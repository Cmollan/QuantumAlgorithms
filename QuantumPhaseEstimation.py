# Code created by Calahan Mollan

def qpe(circuit, start_count_qubit, stop_count_qubit, measure_qubit, theta):
    # SUMMARY: Estimate (in terms of binary fractions represented in the Fourier basis) the phase of the indicated qubit
    # INPUT: curcuit - a Qiskit QuantumCircuit object on which to preform the estimation
    #        start_count_qubit - index of the start of the count qubits on which to store the binary fraction information
    #        stop_count_qubit - index of the end of the count qubits on which to store the binary fraction information
    #        measure_qubit - the index of the qubit which is being estimated
    #        theta - the angle which to rotate
    # OUTPUTS: circuit - Qiskit QuantumCirciut with the gates for the estimation added

    for qubit in range(start_count_qubit, stop_count_qubit + 1):
        circuit.h(qubit)

        circuit.cu1(2**(qubit-start_count_qubit)*theta,
                    qubit,
                    measure_qubit)

    circuit.barrier()

    return circuit


def inv_qpe(circuit, start_count_qubit, stop_count_qubit, measure_qubit, theta):
    # SUMMARY: Estimate the qubit when given the (in terms of binary fractions represented in the Fourier basis) phase
    # INPUT: curcuit - a Qiskit QuantumCircuit object on which to preform the estimation
    #        start_count_qubit - index of the start of the count qubits on which to store the binary fraction information
    #        stop_count_qubit - index of the end of the count qubits on which to store the binary fraction information
    #        measure_qubit - the index of the qubit which is being estimated
    #        theta - the angle which to rotate
    # OUTPUTS: circuit - Qiskit QuantumCirciut with the gates for the estimation added

    for qubit in range(stop_count_qubit, start_count_qubit - 1, -1):

        circuit.cu1(2**(qubit - start_count_qubit)*-theta,
                    qubit,
                    measure_qubit)

    for qubit in range(start_count_qubit, stop_count_qubit + 1):
        circuit.h(qubit)
    circuit.h(measure_qubit)

    circuit.barrier()
    return circuit
