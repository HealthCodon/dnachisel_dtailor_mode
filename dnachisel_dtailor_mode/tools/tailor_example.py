from dnachisel.builtin_specifications import EnforceTranslation
from dnachisel.builtin_specifications.EnforceTranslation import \
    EnforceTranslation
from dnachisel.DnaOptimizationProblem import DnaOptimizationProblem
from dnachisel.Location import Location
from dnachisel.Specification import SpecEvaluation, Specification
from dnachisel.tools import Range, RangeSet, analyze_cai
from dnachisel.tools.Design import DesignSpace, FullFactorial, Optimization
from dnachisel.tools.SequenceDesigner import SequenceDesigner


class CAI(Specification):


    def __init__(self, location=None, boost=1.0):
        """Initialize."""
        self.location = Location.from_data(location)
        self.boost = boost

    def initialized_on_problem(self, problem, role=None):
        return self._copy_with_full_span_if_no_location(problem)

    def evaluate(self, problem):
        """Find matches and count them negatively"""
        location = self.location
        if location is None:
            location = Location(0, len(problem.sequence))
        sequence = location.extract_sequence(problem.sequence)
        

        score = analyze_cai(sequence)

        return SpecEvaluation(
            self,
            problem,
            score=score,
            locations=[location],
            message="CAI: %s at %s" % (score, location),
        )

class GCContent(Specification):
    def __init__(self, location=None, boost=1.0):
        """Initialize."""
        self.location = Location.from_data(location)
        self.boost = boost

    def initialized_on_problem(self, problem, role=None):
        return self._copy_with_full_span_if_no_location(problem)

    def evaluate(self, problem):
        """Find matches and count them negatively"""
        location = self.location
        if location is None:
            location = Location(0, len(problem.sequence))
        sequence = location.extract_sequence(problem.sequence)
        
        
        num_G = sequence.count('G')
        num_C = sequence.count('C')
        
        score = (num_C + num_G) / len(sequence)

        return SpecEvaluation(
            self,
            problem,
            score=score,
            locations=[location],
            message="GC: %s at %s" % (score, location),
        )
    
    


class myDesigner(SequenceDesigner):

    def define_problem(self, sequence,solution_id):
        problem = DnaOptimizationProblem(
            sequence =sequence,
            solution_id = solution_id,
#             constraints = [
#                 EnforceTranslation(),
#             ],
            design_space = self.design_space
        )
        
        return problem

design =   FullFactorial(
# design =      Optimization(
        ['cai','gc'],
        [CAI(),GCContent()],
        [RangeSet([(1, Range(0,0.06)),(3, Range(0.06,0.07)),(2, Range(0.07,1))]),   
         RangeSet([('a', Range(0,0.3)),('b', Range(0.3,0.6)),('c', Range(0.6,1))]) ],
        ['REAL','REAL'],
        target = '2.a'
)

designer = myDesigner(
    "test", 
    'cggcttaactcgagagctgacctgcttctacctagccttacagtggtaacgacccaatctgcgtagcgcaacgca', 
    design, 
    "./test", 
    createDB=True
)

designer.run()
