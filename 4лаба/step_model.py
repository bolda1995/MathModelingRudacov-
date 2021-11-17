import random


def step_model(generator, processor, total_tasks=0, repeat_percent=0, step=0.001):
    processed_tasks = 0  # - количество выполненных заданий
    t_curr = step  # - время в данный момент
    t_gen = generator.generate()  # - время сообщения от генератора
    t_gen_prev = t_proc = 0  # - время предыдущего сообщения и время до следующего
    cur_queue_len = max_queue_len = 0  # - длина очереди сообщений и максимальная длина очереди
    free = True  # - датчик занятости обслуживающего аппарата

    while processed_tasks < total_tasks:
        # Генератор                               - выдача генератором сообщений за данный шаг времени
        # if t_curr > t_gen:                       - старая проверка, я не уверен, правильно ли вызывать её только один раз за такт
        while t_curr > t_gen:  # - проверка, нужно ли генереровать новое сообщение от генератора
            cur_queue_len += 1
            if cur_queue_len > max_queue_len:
                max_queue_len = cur_queue_len
            t_gen_prev = t_gen
            t_gen += generator.generate()

        # Обработчик                              - обработка сообщений обслуживающим аппаратом
        if t_curr > t_proc:  # - проверка, чтобы ничего не делать, пока аппарат занят
            if cur_queue_len > 0:
                was_free = free  # - запоминаем для правильного обновления time_proc
                if free:  # - Если аппарат был свободен
                    free = False  # - то теперь будет занят
                else:  # - А если был занят, то он выполнил свою задачу
                    processed_tasks += 1  # - можно увеличить счётчик обработанных сообщений
                    if random.randint(1,
                                      100) <= repeat_percent:  # - здесь происходит процентная подача сообщений обратно в очередь
                        cur_queue_len += 1
                cur_queue_len -= 1  # - уменьшаем длину очереди сообщений
                if was_free:  # - обновление time_proc
                    t_proc = t_gen_prev + processor.generate()  # - если аппарат был свободен, то он только обрабатывал какое-то сообщение (а потом прокрастинировал)
                else:
                    t_proc += processor.generate()  # - а если занят, то занялся следующим сообщением сразу после предыдущего
            else:
                free = True  # - если сообщения закончились, аппарат свободен

        t_curr += step  # - следующий такт времени.

    return max_queue_len
