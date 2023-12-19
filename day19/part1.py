#!/usr/bin/env python3
import re
import time


class Workflow:
    def __init__(self, workflow_id, rules, default_target):
        self.workflow_id = workflow_id
        self.rules = rules
        self.default_target = default_target

    def process(self, part):
        for (category, op, value, target) in self.rules:
            if eval(f'{part[category]} {op} {value}'):
                return target
        return self.default_target

    def process_interval(self, part):
        for (category, op, value, target) in self.rules:
            if eval(f'{part[category][0]} {op} {value}') and eval(f'{part[category][1]} {op} {value}'):
                # the entire range verifies the condition
                return target, [part]
            elif not eval(f'{part[category][0]} {op} {value}') and not eval(f'{part[category][1]} {op} {value}'):
                # the entire range does not verify the condition
                continue
            else:
                # we split the range in 2 : one part that verifies and one part that does not verify the condition
                part1, part2 = dict(part), dict(part)
                limit = value if op == '>' else value - 1
                part1[category] = part[category][0], limit
                part2[category] = limit + 1, part[category][1]
                return self.workflow_id, [part1, part2]
        return self.default_target, [part]


def parse(input_path):
    with open(input_path, 'r') as f:
        workflows, parts = {}, []
        workflows_block, parts_block = f.read().split('\n\n')
        for line in workflows_block.split('\n'):
            workflow_id, rules_str = re.match(r"^(\w+){(.*)}$", line).groups()
            rules = []
            for rule in rules_str.split(','):
                if ':' in rule:
                    category, op, value, target = re.match(r'^(\w+)([><])(\d+):(.*)$', rule).groups()
                    rules.append((category, op, int(value), target))
                else:
                    default = rule
            workflows[workflow_id] = Workflow(workflow_id, rules, default)
        for line in parts_block.split('\n'):
            categories = {}
            for block in line[1:-1].split(','):
                category, value = re.match(r"^(\w+)=(.*)$", block).groups()
                categories[category] = int(value)
            parts.append(categories)
        return workflows, parts


def solve(workflows, parts):
    score = 0
    for part in parts:
        workflow_id = 'in'
        while workflow_id not in ['A', 'R']:
            workflow_id = workflows[workflow_id].process(part)
        if workflow_id == 'A':
            score += sum([part[category] for category in part])
    return score


if __name__ == "__main__":
    start = time.time()
    workflows, parts = parse("data.txt")
    result = solve(workflows, parts)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
