from datetime import datetime


def log(filename=str()):
    def wrapper(my_fuction):  # передал сюда функцию
        def inner(*args, **kwargs):
            start_1 = datetime.now()
            time_true = start_1.strftime("[%Y-%m-%d %H:%M:%S]")
            try:
                true_func_result = my_fuction(*args, **kwargs)
            except Exception as error:
                time_error = datetime.now()
                time_oshibka = time_error.strftime("[%Y-%m-%d %H:%M:%S]")
                yvedomlyniye = f"{time_true} {my_fuction.__name__}, started with inputs: {(*args,), {**kwargs, }}"
                yvedomlyniye2 = f"{time_oshibka} {my_fuction.__name__}, error {error}: : {(*args,), {**kwargs, }}"
                if not filename:
                    print(yvedomlyniye, yvedomlyniye2, sep="\n")
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{yvedomlyniye}\n")
                        file.write(f"{yvedomlyniye2}\n")
                raise error

            start_2 = datetime.now()
            finish_time = start_2.strftime("[%Y-%m-%d %H:%M:%S]")
            if not filename:
                print(time_true, end=" ")
                print(f"{my_fuction.__name__}, started with inputs: {(*args,), {**kwargs, }}")
                print(finish_time, end=" ")
                print(f"{my_fuction.__name__}, finished successfully with result: {true_func_result}")
                return true_func_result
            else:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(f"{time_true} {my_fuction.__name__}, started with inputs: {(*args,), {**kwargs, }} \n")
                    file.write(
                        f"{finish_time} {my_fuction.__name__}, "
                        f"finished successfully with result: {true_func_result} \n"
                    )

        return inner

    return wrapper
