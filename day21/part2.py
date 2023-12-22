#!/usr/bin/env python3
import math
import time
from collections import deque
from part1 import parse, init_modules

# This part requires to observe the input file, and is possibly specific to my custom input file.
# We notice that the 'rx' module can receive pulses only from the 'zh' module.
# 'zh' is a conjunctive module, so it sends a high pulse only when the last pulse received from each sender is high.
# Everytime a pulse is sent to 'rx', we observe the last pulse received by 'zh' from each of its senders.
# We notice that each of its sender sends a high pulse periodically (every X button press).
# The period is different for each of 'zh' module's senders.
# Therefore, all senders will send a high pulse on the button press that is a common multiplier of all the periods.
# So the fewest button press to reach this state is the LCM of all the periods of 'zh' module's senders.


def solve(modules):
    init_modules(modules)
    i = 0
    periods = { sender_name: 0 for sender_name in modules['zh'].received }
    while True:
        i += 1
        to_process = deque([('broadcaster', 0, 'BUTTON')])
        while len(to_process):
            module_name, received_pulse, sender_name = to_process.popleft()
            generated_pulse = modules[module_name].process(received_pulse, sender_name)
            if generated_pulse != -1:
                for target in modules[module_name].targets:
                    to_process.append((target, generated_pulse, module_name))

            # when 'rx' receives a pulse, we check the last pulse received from each sender of the 'zh' module
            # the first time it is a high pulse gives us the period for each sender
            if 'rx' in modules[module_name].targets:
                for zh_sender in periods:
                    if periods[zh_sender] == 0 and modules['zh'].received[zh_sender] == 1:
                        periods[zh_sender] = i
                        if 0 not in periods.values():
                            # we found the period for all senders
                            return math.lcm(*periods.values())


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve(parsed)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
