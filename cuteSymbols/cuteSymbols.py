
import re
from typing import List, Tuple, Optional, Dict


class CuteSymbols:

    class State:
        CHECK = "✅"
        CROSS = "❌"
        WARNING = "⚠️"
        INFO = "ℹ️"
        SUCCESS = "✔️"
        FAILURE = "✖️"
        QUESTION = "❓"

    class Activity:
        ROCKET = "🚀"
        LOOP = "🔄"
        CLOCK = "⏱️"
        HOURGLASS = "⏳"
        FLASH = "⚡"

    class Emotion:
        THINK = "🤔"
        BRAIN = "🧠"
        LIGHT = "💡"
        FIRE = "🔥"
        MAGIC = "✨"
        STAR = "⭐"
        EYES = "👀"

    class Objects:
        FOLDER = "📁"
        GEAR = "⚙️"
        TOOL = "🛠️"
        BUG = "🐞"

    # Proxy access: CuteSymbols.FIRE, CuteSymbols.CHECK, etc.
    def __getattr__(self, name: str) -> str:
        """
                Allow direct access to symbols via attribute syntax.

                Args:
                    name: Symbol name

                Returns:
                    The emoji symbol

                Raises:
                    AttributeError: If symbol is not found
                """

        for group in [self.State, self.Activity, self.Emotion, self.Objects]:
            if hasattr(group, name):
                return getattr(group, name)
        raise AttributeError(f"Name not found: '{name}'")

    def __dir__(self) -> List[str]:
        """
                Return list of available symbol names for autocomplete.

                Returns:
                    List of all available symbol names
                """

        names = set()
        for group in [self.State, self.Activity, self.Emotion, self.Objects]:
            names.update(
                name for name, val in vars(group).items()
                if not name.startswith("_") and isinstance(val, str)
            )
        return sorted(names | self.__dict__.keys())

    @staticmethod
    def info_from_emoji(emoji) -> Optional[Tuple[str, str]]:
        """
        Extracts and returns information about an emoji, including its name and group, from the list of
        stored emojis. If the emoji is not found among the stored entries, returns None.

        Example: print(CuteSymbols.info_from_emoji("🔥"))      # ("FIRE", "Emotion")

        :param emoji: The emoji symbol to search for.
        :type emoji: str
        :return: A tuple containing the name and group of the emoji if found, or None if the emoji is not
                 in the collection.
        :rtype: tuple[str, str] | None
        :raises AttributeError: If the provided emoji is None.
        """
        if emoji is None:
            raise AttributeError("The symbol can not be None")
        for group, name, value in CuteSymbols.list_all():
            if value == emoji:
                return (name, group)
        return None

    @staticmethod
    def name_from_emoji(emoji) -> Optional[str]:
        """
        Determines the name of a symbol corresponding to the provided emoji. This
        method searches through a predefined listing of symbols and their associated
        values, attempting to locate an entry whose emoji matches the given emoji
        parameter. If a match is found, the corresponding name is returned.

        Example: print(CuteSymbols.name_from_emoji("🔥"))      # "FIRE"

        :param emoji: The emoji to be matched with a symbol name
        :type emoji: str
        :return: The name corresponding to the given emoji if found, otherwise None
        :rtype: str | None
        :raises AttributeError: If the provided emoji parameter is None
        """
        if emoji is None:
            raise AttributeError("The symbol name can not be None")
        for _, name, value in CuteSymbols.list_all():
            if value == emoji:
                return name
        return None  # oppure: raise ValueError(f"Emoji non trovata: {emoji}")

    @staticmethod
    def list_all() -> List[Tuple[str, str, str]]:
        """
        Lists all symbols from multiple groups.

        This method aggregates all string symbols from the defined groups into a
        single list. The groups are iterated through and their member attributes
        are inspected. Attributes starting with an underscore are ignored. Only
        members that are string values are included in the result. The method
        returns a list of tuples where each tuple represents a group name, the
        attribute name within that group, and its corresponding string value.

        :return: A list of tuples containing group name, attribute name, and string value
        :rtype: list[tuple[str, str, str]]
        """
        symbols = []
        for group in [CuteSymbols.State, CuteSymbols.Activity, CuteSymbols.Emotion, CuteSymbols.Objects]:
            group_name = group.__name__
            symbols += [
                (group_name, name, value)
                for name, value in vars(group).items()
                if not name.startswith("_") and isinstance(value, str)
            ]
        return symbols

    @staticmethod
    def print_table():
        """Prints a table with all the available CuteSymbols."""
        print("\n📦  Available CuteSymbols:\n")
        for group, symbol in CuteSymbols._simboli_per_gruppo().items():
            print(f"🔹 {group}")
            for nome, valore in symbol:
                print(f"   {valore}  {nome}")
            print()

    @staticmethod
    def _simboli_per_gruppo() -> Dict[str, List[Tuple[str, str]]]:
        """
        Groups symbols into categories based on their group and returns a dictionary.

        This method iterates through all symbols returned by the CuteSymbols.list_all()
        method. It groups these symbols by their group and constructs a dictionary
        where the keys represent the groups, and the values are lists of tuples. Each
        tuple consists of the name and value of a symbol that belongs to the respective
        group.

        :return: A dictionary mapping group names to lists of tuples, where each tuple
                 contains the symbol name and its associated value.
        :rtype: dict
        """
        grouped = {}
        for group, name, value in CuteSymbols.list_all():
            grouped.setdefault(group, []).append((name, value))
        return grouped

    @staticmethod
    def search(pattern, flags=re.IGNORECASE) -> List[Tuple[str, str, str]]:
        """
        Searches for symbols that match the given query in their name or value. The method strips and
        converts the query to lowercase for case-insensitive search. It compares the query against the
        symbol names and values provided by the `CuteSymbols.list_all()` method. If matches are found,
        they are added to a list that is returned as the result.

        Examples:
            CuteSymbols.search("fir") # returns all symbols that contain "fir"
            CuteSymbols.search("🔥") # returns ['Emotion', 'FIRE', '🔥']
            CuteSymbols.search(r"^F") # returns all symbols that start with "F"
            CuteSymbols.search(r".*O.*O.*") # returns all symbols that contain two "O"s

        :param pattern: The search query string to identify matching symbols.
        :type pattern: str
        :param flags: Regex flags to apply to the search.
        :type flags: int
        :return: A list of tuples where each tuple represents a matching symbol and contains
            group, name, and value related to the symbol.
        :rtype: list[tuple[str, str, str]]
        :raises AttributeError: If the pattern is None.
        """
        if pattern is None:
            raise AttributeError("The pattern can not be None")
        elif not pattern:
            return [(group, name, value) for group, name, value in CuteSymbols.list_all()]

        # Se l'utente non ha specificato flags=0 (case-sensitive), aggiungi IGNORECASE
        if flags != 0:
            flags = flags | re.IGNORECASE

        # Se re.IGNORECASE è incluso nei flags, converti il pattern in lowercase
        # altrimenti mantieni il pattern originale
        if flags & re.IGNORECASE:
            pattern = pattern.strip().lower()
        else:
            pattern = pattern.strip()

        results = []

        try:
            regex = re.compile(pattern, flags)
        except re.error as e:
            raise ValueError(f"Pattern regex not valid: {e}")

        for group, name, value in CuteSymbols.list_all():
            # Se re.IGNORECASE è incluso nei flags, converti name in lowercase per la ricerca
            # altrimenti usa il name originale
            search_name = name.lower() if flags & re.IGNORECASE else name

            if regex.search(search_name) or regex.search(value):
                results.append((group, name, value))

        return results
