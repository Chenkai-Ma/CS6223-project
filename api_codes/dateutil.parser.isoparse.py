@_takes_ascii
def isoparse(self, dt_str):
    components, pos = self._parse_isodate(dt_str)

    if len(dt_str) > pos:
        if self._sep is None or dt_str[pos:pos + 1] == self._sep:
            components += self._parse_isotime(dt_str[pos + 1:])
        else:
            raise ValueError('String contains unknown ISO components')

    if len(components) > 3 and components[3] == 24:
        components[3] = 0
        return datetime(*components) + timedelta(days=1)

    return datetime(*components)