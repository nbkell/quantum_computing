import numpy as np
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, assemble, Aer
from qiskit.quantum_info import Statevector
from qiskit.visualization import array_to_latex, state_visualization, plot_state_city, plot_bloch_multivector
import cmath, random

def simulate_circuit(circ, shots=1024):
    ''' 
    Simulates quantum circuit circ shots number of times.
    Parameters: q circuit circ, int shots
    Return Value: result object (stores final state of circuit)
    '''
    sim = Aer.get_backend('aer_simulator')
    circ.save_statevector()
    qobj = assemble(circ)
    result = sim.run(qobj, shots=shots).result()
    return result

def bra_ket_latex(state_vector):
    '''
    Given a state vector object, returns an image object displaying the correspond state in LaTeX.
    Parameters: Statevector state_vector
    Return Value: graphics object displaying state in LaTeX in bra-ket notation.
    '''
    clean_state = Statevector([state_visualization._round_if_close(v) for v in np.asarray(state_vector)])
    return clean_state.draw(output='latex')
