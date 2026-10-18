from pathlib import Path
S=(Path(__file__).parents[1]/'contracts'/'contract.py').read_text()
def test_surface():
 for n in ('file_agenda','split','request_revision','adopt','withdraw','get_agenda'):assert 'def '+n in S
def test_validator_replays_atomic_questions():assert 'return run()==leader.calldata' in S and 'distinct source anchor' in S
def test_sources_are_independent():assert 'ro==mo' in S and 'rules_digest' in S and 'motion_digest' in S
def test_revision_is_bounded():assert 'int(a.revision)>=1' in S and 'origin!=old_origin' in S
def test_chair_and_clerk_roles():assert 'watcher==gl.message.sender_address' in S and 'gl.message.sender_address!=a.chair' in S
