# Code created by Calahan Mollan
from numpy import pi


def quantum_rotation(circuit, start_qubit, stop_qubit):
    # SUMMARY:Recursively adds the gates necessary to translate qubits from the computational basis to the Fourier basis
    # INPUTS: circuit - a Qiskit QuantumCircuit object on which to preform the rotation
    #         start_qubit - the index of the start of the translation
    #         stop_qubit - the index of the end of the translation, recursively changed throughout the function
    # OUTPUTS: circuit - Qiskit QuantumCircuit object now with added gates for the translation.

    if stop_qubit == start_qubit:  # Stop recursion check
        circuit.h(stop_qubit)
        return circuit

    else:

        circuit.h(stop_qubit)

        for i in range(start_qubit, stop_qubit):
            circuit.cu1(pi / 2 ** (stop_qubit - i), i, stop_qubit)

        stop_qubit -= 1  # Decrease stop qubit until recursion stop is triggered when it matches start qubit
        quantum_rotation(circuit, start_qubit, stop_qubit)


def inv_quantum_rotation(circuit, start_qubit, stop_qubit, i=0):
    # SUMMARY:Recursively adds the gates neccesary to translate qubits from the Fourier basis to the computational basis
    # INPUTS: circuit - a Qiskit QuantumCircuit object on which to preform the rotation
    #         start_qubit - the index of the start of the translation
    #         stop_qubit - the index of the end of the translation
    #         i - an input only used by the function itself to complete the recursion
    # OUTPUTS: circuit - Qiskit QuantumCircuit object now with added gates for the translation.

    if start_qubit + i - 1 == stop_qubit:  # Stop recursion check
        return circuit

    else:
        for j in range(i):
            circuit.cu1(-pi/(2**j * 2),
                        start_qubit + i - j - 1,
                        start_qubit + i)

        circuit.h(start_qubit + i)
        i += 1
        inv_quantum_rotation(circuit, start_qubit, stop_qubit, i)


def quantum_register_swap(circuit, start_qubit, stop_qubit):
    # SUMMARY: Swaps significance of bits between the indicated start and stop. Necessary because qiskit is weird
    # INPUTS: circuit - a Qiskit QuantumCircuit object on which to preform the swap
    #         start_qubit - the index of the start of the swap
    #         stop_qubit - the index of the end of the swap
    # OUTPUTS: circuit - Qiskit QuantumCircuit object now with the added swap

    qubit_range = stop_qubit - start_qubit + 1

    for i in range(qubit_range//2):
        circuit.swap(start_qubit + i, stop_qubit - i)

    return circuit


def qft(circuit, start_qubit, stop_qubit):
    # SUMMARY: High-level function that preforms the sub-operations necessary to convert the given range of qubits
    #          from the computational basis to the Fourier basis
    # INPUTS: circuit - a Qiskit QuantumCircuit object on which to preform the translation
    #         start_qubit - the index of the start of the translation
    #         stop_qubit - the index of the stop of the translation
    # OUTPUTS: circuit - Qiskit QuantumCircuit now with the translation complete
    quantum_rotation(circuit, start_qubit, stop_qubit)

    circuit.barrier()  # Not really necessary, just makes it look nicer. Can be removed.

    quantum_register_swap(circuit, start_qubit, stop_qubit)

    return circuit


def inv_qft(circuit, start_qubit, stop_qubit):
    # SUMMARY: High-level function that preforms the sub-operations necessary to convert the given range of qubits
    #          from the Fourier basis to the computational basis
    # INPUTS: circuit - a Qiskit QuantumCircuit object on which to preform the translation
    #         start_qubit - the index of the start of the translation
    #         stop_qubit - the index of the stop of the translation
    # OUTPUTS: circuit - Qiskit QuantumCircuit now with the translation complete

    quantum_register_swap(circuit, start_qubit, stop_qubit)

    inv_quantum_rotation(circuit, start_qubit, stop_qubit)

    return circuit
