from random import randint


def event_model(generator, processor, total_tasks=0, repeat_percent=0):
    processed_tasks = 0                             # - количество выполненных заданий
    cur_queue_len = max_queue_len = 0               # - длина очереди сообщений и максимальная длина очереди
    events = [[generator.generate(), 'g']]          # - события, тип - [время события, флаг]
    free, process_flag = True, False                # - свободность обслуживающего аппарата, необходимость посмотреть следующее задание

    while processed_tasks < total_tasks:
        event = events.pop(0)                       # - Вытаскиваем первое событие
        # Генератор
        if event[1] == 'g':                         # - Если событие от генератора, то
            cur_queue_len += 1                      # - увеличиваем очередь сообщений
            if cur_queue_len > max_queue_len:       # - обновление нужной максимальной очереди
                max_queue_len = cur_queue_len
            add_event(events, [event[0] + generator.generate(), 'g'])       # - добавляем куда-то внутрь новое событие от генератора (add_event)
            if free:                                # - если аппарат (был) свободен, то
                process_flag = True                 # - ему нужно теперь будет посмотреть следующее задание

        # Обработчик
        elif event[1] == 'p':                       # - Если событие от процессора (выполненное сообщение), то
            processed_tasks += 1                    # - увеличиваем счетчик обработанных сообщений
            if randint(1, 100) <= repeat_percent:           # - если задан процент возвращаемых сообщений, то
                cur_queue_len += 1                  # - возвращаем сообщение в очередь
            process_flag = True                     # - И делаем следующим заданием то, которое сразу получили в очередь

        if process_flag:                            # - Если задание для аппарата есть, то
            if cur_queue_len > 0:                   # - если сообщения в очереди есть, то
                cur_queue_len -= 1                  # - надо просмотреть первое
                add_event(events, [event[0] + processor.generate(), 'p'])   # - и сделать событие окончания занятости
                free = False                        # - и сказать, что сейчас обслуживающий аппарат занят
            else:
                free = True                         # - а если сообщений нет, то аппарат может быть свободен
            process_flag = False                    # - и необходимость работы аппарата убрать, она появится из-за других событий

    return max_queue_len                            # - Возращение максимальной длины очереди


def add_event(events, event: list):                 # - Добавление события в последовательность событий
    c = -1
    for i in range(len(events)):
        if events[i][0] >= event[0]:
            c = i
            break
        # - Ищем место события по временной шкале между другими событиями
    if c == -1:
        c == len(events)

    if 0 < c < len(events):
        events.insert(c - 1, event)                 # - Добавляем событие куда нужно
    else:
        events.insert(c, event)
