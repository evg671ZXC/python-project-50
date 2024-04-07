stylish_nested_check = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
         key: value
         }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""


plain_nested_check = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""

json_nested_check = """{"common": {"state": "NESTED", "value": {"follow": {"state": "ADDED", "value": false}, "setting1": {"state": "UNCHANGED", "value": "Value 1"}, "setting2": {"state": "REMOVED", "value": 200}, "setting3": {"state": "CHANGED", "value": null, "old_value": true}, "setting4": {"state": "ADDED", "value": "blah blah"}, "setting5": {"state": "NESTED", "sub_state": "ADDED", "value": {"key5": {"state": "UNCHANGED", "value": "value5"}}}, "setting6": {"state": "NESTED", "value": {"doge": {"state": "NESTED", "value": {"wow": {"state": "CHANGED", "value": "so much", "old_value": ""}}}, "key": {"state": "UNCHANGED", "value": "value"}, "ops": {"state": "ADDED", "value": "vops"}}}}}, "group1": {"state": "NESTED", "value": {"baz": {"state": "CHANGED", "value": "bars", "old_value": "bas"}, "foo": {"state": "UNCHANGED", "value": "bar"}, "nest": {"state": "CHANGED", "value": "str", "old_value": {"key": "value"}}}}, "group2": {"state": "NESTED", "sub_state": "REMOVED", "value": {"abc": {"state": "UNCHANGED", "value": 12345}, "deep": {"state": "NESTED", "value": {"id": {"state": "UNCHANGED", "value": 45}}}}}, "group3": {"state": "NESTED", "sub_state": "ADDED", "value": {"deep": {"state": "NESTED", "value": {"id": {"state": "NESTED", "value": {"number": {"state": "UNCHANGED", "value": 45}}}}}, "fee": {"state": "UNCHANGED", "value": 100500}}}}"""
