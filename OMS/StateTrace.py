class StateTrace:
    def nextState(self, current_state, input):
        state_transition_table = [
            [0, 0, 2, 21],
            [0, 0, 3, 21],
            [0, 0, 4, 21],
            [0, 0, 5, 21],
            [7, 6, 0, 21],
            [0, 0, 2, 21],
            [0, 0, 8, 21],
            [0, 9, 10, 21],
            [0, 0, 2, 21],
            [0, 0, 11, 21],
            [0, 0, 12, 21],
            [0, 0, 13, 21],
            [0, 0, 14, 21],
            [0, 0, 15, 21],
            [16, 17, 0, 21],
            [0, 0, 18, 21],
            [0, 0, 12, 21],
            [0, 0, 19, 22],
            [0, 0, 20, 21],
            [0, 0, 0, 0],
            [0, 0, 12, 21]
        ]
        # all of the state number is integer
        output_state = state_transition_table[current_state, input]
        return output_state

    def state_translator(self, state):
        # take a state number as input and output a string
        state_string = {
            1: "create",
            2: "dispatching to maker",
            3: "maker founded",
            4: "sent request to maker",
            5: "maker read request",
            6: "maker reject",
            7: "maker accept",
            8: "making",
            9: "maker give up",
            10: "maker finish",
            11: "maker, user check the product",
            12: "finding transporter",
            13: "transporter founded",
            14: "sent request to transporter",
            15: "transporter read request",
            16: "transporter accept",
            17: "transporter reject",
            18: "transporting",
            19: "user recieved",
            20: "finish",
            21: "user give up",
            22: "transporter give up"
        }
