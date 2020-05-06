from .error_nan import error_nan


def clip(array, standard_deviation):

    error_nan(array)

    mean = array.mean()

    margin = array.std() * standard_deviation

    return array.clip(min=mean - margin, max=mean + margin)
