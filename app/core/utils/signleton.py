def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):  # noqa: ANN202
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance
