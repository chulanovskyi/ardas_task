# Tasker
### Prerequisites: Python 3

---

Script will help you to evenly dispatch tasks between a group of employees.

### How to use:
#### Fast run
Run script in terminal to see how it handle a randomly generated workgroup and task list.
By default our group consists of three employees and a 10 tasks list.

##### Output
- Task: `name(task point)(task status)`
**Note!** Task status can be: *0 = available*, *1 = assigned*, *2 = solved*
- Employee: `nickname (task point)(total amount of assigned task points): [assigned tasks]`
```
Task list: [task_1(19)(1), task_2(9)(1), task_3(18)(1), task_4(7)(1), task_5(7)(1),
task_6(12)(1), task_7(13)(1), task_8(14)(1), task_9(14)(1), task_10(6)(1)]

Emp_0 (39)(29): [task_10(6)(1), task_2(9)(1), task_8(14)(1)]
Emp_1 (83)(70): [task_4(7)(1), task_6(12)(1), task_9(14)(1), task_3(18)(1), task_1(19)(1)]
Emp_2 (28)(20): [task_5(7)(1), task_7(13)(1)]

Remained tasks: []
```
---
#### Using as imported module
Instantiate these classes:

- `Task(name, task_point)`
- `Employee(nickname, task_point)`
```
>>>Imp_1 = Employee('Jiws', 50)
>>>Imp_2 = Employee('Dobby', 80)

>>>take_bag = Task('Take bag', 5)
>>>wear_socks = Task('Wear socks', 5)
```

Wrap your instances into appropriate  lists (for example in `lazy_workers` and `easy_tasks`):
```
>>>lazy_workers = [Imp_1, Imp_2]
>>>easy_tasks = [take_bag, wear_socks]
```

Create task dispatcher:

- `Spreader(workgroup, task_list)`
```
>>>spreader = Spreader(lazy_workers, easy_tasks)
```

Spread task between employees:
```
>>>spreader.spread()
```

View result:
```
>>>spreader.print_result()

Task list: [Take bag(5)(1), Wear socks(5)(1)]
Jiws (50)(5): [Take bag(5)(1)]
Dobby (80)(5): [Wear socks(5)(1)]
Remained tasks: []
```

Also you can use help functions such as `generate_group(workers_num)` and `generate_tasks(tasks_num)`
to check different cases.