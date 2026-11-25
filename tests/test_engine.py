import unittest
from src.engine import summarize,keywords,flashcards,quiz,study_plan
class TestEngine(unittest.TestCase):
 def test_summary(self):self.assertTrue(summarize('Python is a popular programming language. It supports multiple programming paradigms.'))
 def test_keywords(self):self.assertIn('python',keywords('Python Python is useful'))
 def test_flashcards(self):self.assertEqual(len(flashcards('Python is a programming language used for automation.')),1)
 def test_quiz(self):self.assertTrue(quiz('Python is a widely used programming language for building software.'))
 def test_plan(self):self.assertEqual(len(study_plan('Python, AI',7)),7)
 def test_empty(self):self.assertEqual(study_plan('',5),[])
if __name__=='__main__':unittest.main()
