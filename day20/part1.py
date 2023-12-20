#!/usr/bin/env python3
import re
import time
from collections import deque


class Module:
    def __init__(self, name, type, targets):
        self.name = name
        self.type = type
        self.targets = targets
        self.on = False          # only relevant when type is %
        self.received = {}       # only relevant when type is &

    def process(self, pulse, sender_name):
        if self.type == '':
            return pulse
        elif self.type == '%' and pulse == 0:
            self.on = not self.on
            return 1 if self.on else 0
        elif self.type == '&':
            self.received[sender_name] = pulse
            return 0 if all([self.received[x] == 1 for x in self.received]) else 1
        return -1


def parse(input_path):
    with open(input_path, 'r') as f:
        modules = {}
        for line in f.read().split('\n'):
            type, name, targets = re.match(r'^([%&]?)(\w+) -> (.+)$', line).groups()
            modules[name] = Module(name, type, targets.split(', '))
        return modules


def init_modules(modules):
    names = [name for name in modules]  # must get it before the for loop as we create new modules in the loop
    for module_name in names:
        for target_name in modules[module_name].targets:
            # create target if it does not have a rule for it (like 'output' in example or 'rx' in real input)
            if target_name not in modules:
                modules[target_name] = Module(target_name, 'x', [])  # type 'x' does nothing
            # initialize the last received pulse for conjunction modules
            if modules[target_name].type == '&':
                modules[target_name].received[module_name] = 0


def solve(modules):
    init_modules(modules)
    pulses_sent = {0: 0, 1: 0}
    for i in range(1000):
        to_process = deque([('broadcaster', 0, 'BUTTON')])
        while len(to_process):
            module_name, received_pulse, sender_name = to_process.popleft()
            generated_pulse = modules[module_name].process(received_pulse, sender_name)
            if generated_pulse != -1:
                for target in modules[module_name].targets:
                    pulses_sent[generated_pulse] += 1
                    to_process.append((target, generated_pulse, module_name))
    return pulses_sent[1] * (1000 + pulses_sent[0])


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve(parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
