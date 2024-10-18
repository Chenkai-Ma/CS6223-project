def adjusted(self):
    try:
        return self._exp + len(self._int) - 1
    # If NaN or Infinity, self._exp is string
    except TypeError:
        return 0