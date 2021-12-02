# IO-bound

## синхронная проверка:
![Getting Started](images/IO-bound_start_and_task_manager_1_workers.png)
![Getting Started](images/IO-bound_profile_1_workers.png)

## 5 воркеров:
![Getting Started](images/IO-bound_start_and_task_manager_5_workers.png)
![Getting Started](images/IO-bound_profile_5_workers.png)

## 10 воркеров:
![Getting Started](images/IO-bound_start_and_task_manager_10_workers.png)
![Getting Started](images/IO-bound_profile_10_workers.png)

## 100 воркеров:
![Getting Started](images/IO-bound_start_and_task_manager_100_workers.png)
![Getting Started](images/IO-bound_profile_100_workers.png)


С увеличением количества потоков увеличивается нагрузка на процессор , нагрузка на память практически не меняется, а нагрузка на сеть увеличивалась постепенно, пропорциально увеличению нагрузки. Время работы уменьшалось.
# CPU-bound.

## генерация на 1 ядре:
![Getting Started](images/CPU-bound_start_and_task_manager_1_workers.png)
![Getting Started](images/CPU-bound_profile_1_workers.png)

## 2 воркерa:
![Getting Started](images/CPU-bound_start_and_task_manager_2_workers.png)
![Getting Started](images/CPU-bound_profile_2_workers.png)

## 4 воркерa:
![Getting Started](images/CPU-bound_start_and_task_manager_4_workers.png)
![Getting Started](images/CPU-bound_profile_4_workers.png)

## 5 воркеров:
![Getting Started](images/CPU-bound_start_and_task_manager_5_workers.png)
![Getting Started](images/CPU-bound_profile_5_workers.png)

## 10 воркеров:
![Getting Started](images/CPU-bound_start_and_task_manager_10_workers.png)
![Getting Started](images/CPU-bound_profile_10_workers.png)

Я делал снэпшоты после генерации одной монеты. Большее количество воркеров немного увеличивает скорость, но так же увеличивает нагрузку.
Последнее увеличение количества воркеров бессмысленно. Уменьшение разницы видно уже в случае 4 и 5 воркеров. В случае 10 воркеров мне вообще не повезло и искалось в разы дольше даже чем с 4 воркерами. Так что увеличение воркеров настолько не показало своей эффективности, в отличии от 1 задачи.