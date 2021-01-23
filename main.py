# example ci/cd using python and github actions

def welcome_message(name: str) -> str:
    if type(name) != str:
        raise ValueError(f"Got type {type(name)}, expected string")
    else:
        res = f"Welcome {name} to the future of QA of software!"
        print(res)
        return res
