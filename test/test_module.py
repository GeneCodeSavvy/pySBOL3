import unittest

import sbol3

OM_KILOGRAM = 'http://www.ontology-of-units-of-measure.org/resource/om-2/kilogram'


class TestModule(unittest.TestCase):

    def test_data_model(self):
        self.assertIsInstance(sbol3.Identified, type)
        self.assertIsInstance(sbol3.TopLevel, type)
        self.assertIsInstance(sbol3.Sequence, type)
        self.assertIsInstance(sbol3.Component, type)
        self.assertIsInstance(sbol3.SubComponent, type)
        self.assertIsInstance(sbol3.ComponentReference, type)
        self.assertIsInstance(sbol3.LocalSubComponent, type)
        self.assertIsInstance(sbol3.ExternallyDefined, type)
        self.assertIsInstance(sbol3.SequenceFeature, type)
        self.assertIsInstance(sbol3.Range, type)
        self.assertIsInstance(sbol3.Cut, type)
        self.assertIsInstance(sbol3.EntireSequence, type)
        self.assertIsInstance(sbol3.Constraint, type)
        self.assertIsInstance(sbol3.Interaction, type)
        self.assertIsInstance(sbol3.Participation, type)
        self.assertIsInstance(sbol3.Interface, type)
        self.assertIsInstance(sbol3.CombinatorialDerivation, type)
        self.assertIsInstance(sbol3.VariableComponent, type)
        self.assertIsInstance(sbol3.Implementation, type)
        self.assertIsInstance(sbol3.ExperimentalData, type)
        self.assertIsInstance(sbol3.Model, type)
        self.assertIsInstance(sbol3.Collection, type)
        self.assertIsInstance(sbol3.Namespace, type)
        self.assertIsInstance(sbol3.Experiment, type)
        self.assertIsInstance(sbol3.Attachment, type)

    def test_provenance(self):
        self.assertIsInstance(sbol3.Activity, type)
        self.assertIsInstance(sbol3.Association, type)
        self.assertIsInstance(sbol3.Plan, type)
        self.assertIsInstance(sbol3.Agent, type)
        self.assertIsInstance(sbol3.Usage, type)

    def test_measurement(self):
        self.assertIsInstance(sbol3.Measure, type)
        self.assertIsInstance(sbol3.SingularUnit, type)
        self.assertIsInstance(sbol3.UnitMultiplication, type)
        self.assertIsInstance(sbol3.UnitDivision, type)
        self.assertIsInstance(sbol3.UnitExponentiation, type)
        self.assertIsInstance(sbol3.PrefixedUnit, type)
        self.assertIsInstance(sbol3.SIPrefix, type)
        self.assertIsInstance(sbol3.BinaryPrefix, type)

    def test_identified_constructors(self):
        # I don't remember why I wanted this test.
        # Test all of the Identified constructors.
        args_map = {
            'Association': ['https://example.com/fake'],
            'ComponentReference': ['https://example.com/fake',
                                   'https://example.com/fake'],
            'Constraint': ['https://example.com/restriction',
                           'https://example.com/subject',
                           'https://example.com/object'],
            'CustomIdentified': ['https://example.com/fake'],
            'Cut': ['https://example.com/fake',
                    1],
            'EntireSequence': ['https://example.com/fake'],
            'ExternallyDefined': [['https://example.com/fake'],
                                  'https://example.com/fake'],
            'Interaction': [['https://example.com/fake']],
            'LocalSubComponent': [['https://example.com/fake']],
            'Measure': [1.0, OM_KILOGRAM],
            'Participation': [sbol3.SBO_INHIBITOR,
                              'https://example.com/fake'],
            'Range': ['https://example.com/fake', 1, 2],
            'SequenceFeature': [[sbol3.EntireSequence('https://example.com/fake')]],
            'SubComponent': ['https://example.com/fake'],
            'Usage': ['https://example.com/fake'],
        }
        for name in dir(sbol3):
            item = getattr(sbol3, name)
            if not isinstance(item, type):
                continue
            if issubclass(item, sbol3.TopLevel):
                continue
            if not issubclass(item, sbol3.Identified):
                continue
            if item == sbol3.Identified:
                continue
            arg_list = []
            if name in args_map:
                arg_list = args_map[name]
            try:
                item(*arg_list)
            except TypeError as e:
                self.fail('Unable to construct sbol3.%s: %s' % (name, e))
            except sbol3.ValidationError as e:
                self.fail('Constructed invalid sbol3.%s: %s' % (name, e))


if __name__ == '__main__':
    unittest.main()
