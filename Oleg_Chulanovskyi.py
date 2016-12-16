from random import randint
from operator import attrgetter

(TASK_AVAILABLE, TASK_ASSIGNED, TASK_SOLVED) = range(0, 3)


class Task:
    def __init__(self, name, task_point):
        self.name = name
        self.task_point = task_point
        self.status = TASK_AVAILABLE

    def __repr__(self):
        return '{n}({t_p})({s})'.format(
            n=self.name,
            t_p=self.task_point,
            s=self.status)


class Employee:
    def __init__(self, nickname, task_point):
        self.nickname = nickname
        self.task_point = task_point
        self.tasks = []

    def get_workload(self):
        workload = sum(task.task_point for task in self.tasks)
        return workload if workload else 0

    def get_remain_points(self):
        return self.task_point - self.get_workload()

    def assign_task(self, task):
        self.tasks.append(task)
        task.status = TASK_ASSIGNED

    def __str__(self):
        return '{n} ({t_p})({w}): {t}'.format(
            n=self.nickname,
            t_p=self.task_point,
            w=self.get_workload(),
            t=self.tasks)


class Spreader:
    def __init__(self, workgroup, task_list):
        self.workgroup = workgroup
        self.task_list = task_list

    def spread(self):
        available_tasks = self.get_available_tasks(self.task_list)

        try:
            simplest = self.get_simplest_task(available_tasks)
        except ValueError:
            print('No available tasks')
            return

        available_employees = list(filter(
            lambda e: e.get_remain_points() > simplest.task_point,
            self.workgroup))

        while available_tasks and available_employees:
            least_busy = self.get_least_busy(available_employees)
            simplest = self.get_simplest_task(available_tasks)
            if simplest.task_point > least_busy.get_remain_points():
                available_employees.remove(least_busy)
                continue
            least_busy.assign_task(simplest)
            available_tasks.remove(simplest)

    @staticmethod
    def get_available_tasks(from_list):
        return list(filter(lambda t: t.status == TASK_AVAILABLE, from_list))

    @staticmethod
    def get_least_busy(from_group):
        return min(from_group, key=lambda e: e.get_workload())

    def get_simplest_task(self, from_list):
        available_tasks = self.get_available_tasks(from_list)
        return min(available_tasks, key=attrgetter('task_point'))

    def print_result(self):
        print('Task list: %s' % self.task_list)
        for emp in self.workgroup:
            print(emp)
        print('Remained tasks: %s' % self.get_available_tasks(self.task_list))


def generate_group(workers_num):
    return [Employee('Emp_%d' % e, randint(20, 100)) for e in range(workers_num)]


def generate_tasks(tasks_num):
    return [Task('task_%d' % (t+1), randint(1, 20)) for t in range(tasks_num)]


if __name__ == '__main__':
    random_group = generate_group(3)
    random_tasks = generate_tasks(10)
    spreader = Spreader(random_group, random_tasks)
    spreader.spread()
    spreader.print_result()
