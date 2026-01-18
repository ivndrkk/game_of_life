from main import next_board_state, dead_state 

def test_dead_stays_dead():
    init = [[0,0,0], [0,0,0], [0,0,0]]
    assert next_board_state(init) == init, "Dead cells stay dead"
    print("PASSED: dead stays dead")

def test_dead_with_3_becomes_alive():
    init = [[0,0,1], [0,1,1], [0,0,0]]
    expected = [[0,1,1], [0,1,1], [0,0,0]]
    assert next_board_state(init) == expected, "Dead cell with 3 live neighbors becomes alive"
    print("PASSED: reproduction")

if __name__ == "__main__":
    test_dead_stays_dead()
    test_dead_with_3_becomes_alive()
    print("All tests OK!")
