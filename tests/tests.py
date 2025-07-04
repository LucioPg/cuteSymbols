import unittest
import re
from cuteSymbols.cuteSymbols import CuteSymbols


class TestCuteSymbols(unittest.TestCase):
    """Test suite completa per la classe CuteSymbols."""

    def setUp(self):
        """Configura l'ambiente di test."""
        self.cute_symbols = CuteSymbols()

    def test_state_symbols(self):
        """Testa tutti i simboli della classe State."""
        self.assertEqual(CuteSymbols.State.CHECK, "✅")
        self.assertEqual(CuteSymbols.State.CROSS, "❌")
        self.assertEqual(CuteSymbols.State.WARNING, "⚠️")
        self.assertEqual(CuteSymbols.State.INFO, "ℹ️")
        self.assertEqual(CuteSymbols.State.SUCCESS, "✔️")
        self.assertEqual(CuteSymbols.State.FAILURE, "✖️")
        self.assertEqual(CuteSymbols.State.QUESTION, "❓")

    def test_activity_symbols(self):
        """Testa tutti i simboli della classe Activity."""
        self.assertEqual(CuteSymbols.Activity.ROCKET, "🚀")
        self.assertEqual(CuteSymbols.Activity.LOOP, "🔄")
        self.assertEqual(CuteSymbols.Activity.CLOCK, "⏱️")
        self.assertEqual(CuteSymbols.Activity.HOURGLASS, "⏳")
        self.assertEqual(CuteSymbols.Activity.FLASH, "⚡")

    def test_emotion_symbols(self):
        """Testa tutti i simboli della classe Emotion."""
        self.assertEqual(CuteSymbols.Emotion.THINK, "🤔")
        self.assertEqual(CuteSymbols.Emotion.BRAIN, "🧠")
        self.assertEqual(CuteSymbols.Emotion.LIGHT, "💡")
        self.assertEqual(CuteSymbols.Emotion.FIRE, "🔥")
        self.assertEqual(CuteSymbols.Emotion.MAGIC, "✨")
        self.assertEqual(CuteSymbols.Emotion.STAR, "⭐")
        self.assertEqual(CuteSymbols.Emotion.EYES, "👀")

    def test_objects_symbols(self):
        """Testa tutti i simboli della classe Objects."""
        self.assertEqual(CuteSymbols.Objects.FOLDER, "📁")
        self.assertEqual(CuteSymbols.Objects.GEAR, "⚙️")
        self.assertEqual(CuteSymbols.Objects.TOOL, "🛠️")
        self.assertEqual(CuteSymbols.Objects.BUG, "🐞")

    def test_getattr_proxy_access(self):
        """Testa l'accesso proxy tramite __getattr__."""
        # Test accesso diretto ai simboli
        self.assertEqual(self.cute_symbols.FIRE, "🔥")
        self.assertEqual(self.cute_symbols.CHECK, "✅")
        self.assertEqual(self.cute_symbols.ROCKET, "🚀")
        self.assertEqual(self.cute_symbols.FOLDER, "📁")

        # Test per tutti i simboli
        self.assertEqual(self.cute_symbols.CROSS, "❌")
        self.assertEqual(self.cute_symbols.WARNING, "⚠️")
        self.assertEqual(self.cute_symbols.INFO, "ℹ️")
        self.assertEqual(self.cute_symbols.SUCCESS, "✔️")
        self.assertEqual(self.cute_symbols.FAILURE, "✖️")
        self.assertEqual(self.cute_symbols.QUESTION, "❓")

        self.assertEqual(self.cute_symbols.LOOP, "🔄")
        self.assertEqual(self.cute_symbols.CLOCK, "⏱️")
        self.assertEqual(self.cute_symbols.HOURGLASS, "⏳")
        self.assertEqual(self.cute_symbols.FLASH, "⚡")

        self.assertEqual(self.cute_symbols.THINK, "🤔")
        self.assertEqual(self.cute_symbols.BRAIN, "🧠")
        self.assertEqual(self.cute_symbols.LIGHT, "💡")
        self.assertEqual(self.cute_symbols.MAGIC, "✨")
        self.assertEqual(self.cute_symbols.STAR, "⭐")
        self.assertEqual(self.cute_symbols.EYES, "👀")

        self.assertEqual(self.cute_symbols.GEAR, "⚙️")
        self.assertEqual(self.cute_symbols.TOOL, "🛠️")
        self.assertEqual(self.cute_symbols.BUG, "🐞")

    def test_getattr_attribute_error(self):
        """Testa che __getattr__ sollevi AttributeError per attributi inesistenti."""
        with self.assertRaises(AttributeError) as context:
            self.cute_symbols.NONEXISTENT
        self.assertIn("Name not found: 'NONEXISTENT'", str(context.exception))

        with self.assertRaises(AttributeError) as context:
            self.cute_symbols.INVALID_SYMBOL
        self.assertIn("Name not found: 'INVALID_SYMBOL'", str(context.exception))

    def test_dir_method(self):
        """Testa il metodo __dir__."""
        expected_names = {
            'CHECK', 'CROSS', 'WARNING', 'INFO', 'SUCCESS', 'FAILURE', 'QUESTION',
            'ROCKET', 'LOOP', 'CLOCK', 'HOURGLASS', 'FLASH',
            'THINK', 'BRAIN', 'LIGHT', 'FIRE', 'MAGIC', 'STAR', 'EYES',
            'FOLDER', 'GEAR', 'TOOL', 'BUG'
        }

        dir_result = set(dir(self.cute_symbols))
        self.assertTrue(expected_names.issubset(dir_result))

    def test_info_from_emoji_valid(self):
        """Testa info_from_emoji con emoji valide."""
        self.assertEqual(CuteSymbols.info_from_emoji("🔥"), ("FIRE", "Emotion"))
        self.assertEqual(CuteSymbols.info_from_emoji("✅"), ("CHECK", "State"))
        self.assertEqual(CuteSymbols.info_from_emoji("🚀"), ("ROCKET", "Activity"))
        self.assertEqual(CuteSymbols.info_from_emoji("📁"), ("FOLDER", "Objects"))
        self.assertEqual(CuteSymbols.info_from_emoji("🤔"), ("THINK", "Emotion"))
        self.assertEqual(CuteSymbols.info_from_emoji("⚙️"), ("GEAR", "Objects"))

    def test_info_from_emoji_invalid(self):
        """Testa info_from_emoji con emoji non valide."""
        self.assertIsNone(CuteSymbols.info_from_emoji("🦄"))
        self.assertIsNone(CuteSymbols.info_from_emoji("💩"))
        self.assertIsNone(CuteSymbols.info_from_emoji("🌈"))
        self.assertIsNone(CuteSymbols.info_from_emoji(""))
        self.assertIsNone(CuteSymbols.info_from_emoji("text"))

    def test_name_from_emoji_valid(self):
        """Testa name_from_emoji con emoji valide."""
        self.assertEqual(CuteSymbols.name_from_emoji("🔥"), "FIRE")
        self.assertEqual(CuteSymbols.name_from_emoji("✅"), "CHECK")
        self.assertEqual(CuteSymbols.name_from_emoji("🚀"), "ROCKET")
        self.assertEqual(CuteSymbols.name_from_emoji("📁"), "FOLDER")
        self.assertEqual(CuteSymbols.name_from_emoji("🤔"), "THINK")
        self.assertEqual(CuteSymbols.name_from_emoji("⚙️"), "GEAR")

    def test_name_from_emoji_invalid(self):
        """Testa name_from_emoji con emoji non valide."""
        self.assertIsNone(CuteSymbols.name_from_emoji("🦄"))
        self.assertIsNone(CuteSymbols.name_from_emoji("💩"))
        self.assertIsNone(CuteSymbols.name_from_emoji("🌈"))
        self.assertIsNone(CuteSymbols.name_from_emoji(""))
        self.assertIsNone(CuteSymbols.name_from_emoji("text"))

    def test_list_all_structure(self):
        """Testa la struttura del risultato di list_all."""
        all_symbols = CuteSymbols.list_all()

        # Verifica che sia una lista
        self.assertIsInstance(all_symbols, list)

        # Verifica che ogni elemento sia una tupla di 3 elementi
        for symbol in all_symbols:
            self.assertIsInstance(symbol, tuple)
            self.assertEqual(len(symbol), 3)
            group, name, value = symbol
            self.assertIsInstance(group, str)
            self.assertIsInstance(name, str)
            self.assertIsInstance(value, str)

    def test_list_all_content(self):
        """Testa il contenuto di list_all."""
        all_symbols = CuteSymbols.list_all()

        # Verifica che contenga tutti i simboli attesi
        expected_symbols = [
            ("State", "CHECK", "✅"),
            ("State", "CROSS", "❌"),
            ("State", "WARNING", "⚠️"),
            ("State", "INFO", "ℹ️"),
            ("State", "SUCCESS", "✔️"),
            ("State", "FAILURE", "✖️"),
            ("State", "QUESTION", "❓"),
            ("Activity", "ROCKET", "🚀"),
            ("Activity", "LOOP", "🔄"),
            ("Activity", "CLOCK", "⏱️"),
            ("Activity", "HOURGLASS", "⏳"),
            ("Activity", "FLASH", "⚡"),
            ("Emotion", "THINK", "🤔"),
            ("Emotion", "BRAIN", "🧠"),
            ("Emotion", "LIGHT", "💡"),
            ("Emotion", "FIRE", "🔥"),
            ("Emotion", "MAGIC", "✨"),
            ("Emotion", "STAR", "⭐"),
            ("Emotion", "EYES", "👀"),
            ("Objects", "FOLDER", "📁"),
            ("Objects", "GEAR", "⚙️"),
            ("Objects", "TOOL", "🛠️"),
            ("Objects", "BUG", "🐞")
        ]

        for expected in expected_symbols:
            self.assertIn(expected, all_symbols)

    def test_list_all_count(self):
        """Testa che list_all restituisca il numero corretto di simboli."""
        all_symbols = CuteSymbols.list_all()
        expected_count = 23  # 7 + 5 + 7 + 4
        self.assertEqual(len(all_symbols), expected_count)

    def test_simboli_per_gruppo_structure(self):
        """Testa la struttura del risultato di _simboli_per_gruppo."""
        grouped = CuteSymbols._simboli_per_gruppo()

        # Verifica che sia un dizionario
        self.assertIsInstance(grouped, dict)

        # Verifica che contenga tutti i gruppi attesi
        expected_groups = ["State", "Activity", "Emotion", "Objects"]
        for group in expected_groups:
            self.assertIn(group, grouped)

        # Verifica la struttura di ogni gruppo
        for group_name, symbols in grouped.items():
            self.assertIsInstance(symbols, list)
            for symbol in symbols:
                self.assertIsInstance(symbol, tuple)
                self.assertEqual(len(symbol), 2)
                name, value = symbol
                self.assertIsInstance(name, str)
                self.assertIsInstance(value, str)

    def test_simboli_per_gruppo_content(self):
        """Testa il contenuto di _simboli_per_gruppo."""
        grouped = CuteSymbols._simboli_per_gruppo()

        # Verifica contenuto specifico
        self.assertIn(("CHECK", "✅"), grouped["State"])
        self.assertIn(("ROCKET", "🚀"), grouped["Activity"])
        self.assertIn(("FIRE", "🔥"), grouped["Emotion"])
        self.assertIn(("FOLDER", "📁"), grouped["Objects"])

    def test_search_none_pattern(self):
        """Testa che search sollevi AttributeError con pattern None."""
        with self.assertRaises(AttributeError) as context:
            CuteSymbols.search(None)
        self.assertIn("The pattern can not be None", str(context.exception))

    def test_search_empty_string(self):
        """Testa la ricerca con stringa vuota."""
        results = CuteSymbols.search("")
        # Stringa vuota dovrebbe restituire tutti i simboli
        self.assertEqual(len(results), 23)

    def test_search_by_simple_name(self):
        """Testa la ricerca semplice per nome."""
        # Test ricerca case-insensitive
        results = CuteSymbols.search("fire")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], ("Emotion", "FIRE", "🔥"))

        # Test ricerca con maiuscole
        results = CuteSymbols.search("FIRE")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], ("Emotion", "FIRE", "🔥"))

    def test_search_by_emoji(self):
        """Testa la ricerca per emoji."""
        results = CuteSymbols.search("🔥")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], ("Emotion", "FIRE", "🔥"))

        results = CuteSymbols.search("✅")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], ("State", "CHECK", "✅"))

    def test_search_regex_start_of_string(self):
        """Testa la ricerca con regex per inizio stringa."""
        # Trova tutti i simboli che iniziano con "f" (lowercase perché il pattern viene convertito)
        results = CuteSymbols.search("^f")
        expected_results = [
            ("Emotion", "FIRE", "🔥"),
            ("State", "FAILURE", "✖️"),
            ("Objects", "FOLDER", "📁"),
            ("Activity", "FLASH", "⚡")
        ]
        self.assertEqual(len(results), 4)
        for expected in expected_results:
            self.assertIn(expected, results)

    def test_search_regex_end_of_string(self):
        """Testa la ricerca con regex per fine stringa."""
        # Trova tutti i simboli che finiscono con "r" (lowercase)
        results = CuteSymbols.search("r$")
        # Dovrebbe trovare STAR, GEAR, e anche FOLDER (che finisce con "er")
        expected_results = [
            ("Emotion", "STAR", "⭐"),
            ("Objects", "GEAR", "⚙️"),
            ("Objects", "FOLDER", "📁")
        ]
        self.assertEqual(len(results), 3)
        for expected in expected_results:
            self.assertIn(expected, results)

    def test_search_regex_contains_pattern(self):
        """Testa la ricerca con regex per pattern contenuto."""
        # Trova tutti i simboli che contengono due "o" (lowercase)
        results = CuteSymbols.search(".*o.*o.*")
        expected_results = [
            ("Activity", "LOOP", "🔄"),
            ("Objects", "TOOL", "🛠️")
        ]
        self.assertEqual(len(results), 2)
        for expected in expected_results:
            self.assertIn(expected, results)

    def test_search_regex_character_class(self):
        """Testa la ricerca con classi di caratteri regex."""
        # Trova tutti i simboli che contengono vocali consecutive (lowercase)
        results = CuteSymbols.search("[aeiou]{2}")
        # Dovrebbe trovare simboli come "HOURGLASS" che contiene "ou"
        hourglass_found = any(result[1] == "HOURGLASS" for result in results)
        self.assertTrue(hourglass_found)

    def test_search_regex_case_sensitive(self):
        """Testa la ricerca con regex case-sensitive."""
        # Anche con flag case-sensitive, il pattern viene convertito in lowercase
        results = CuteSymbols.search("fire", flags=0)
        self.assertEqual(len(results), 0)  # Non trova nulla perché cerca "fire" ma i nomi sono "FIRE"

    def test_search_regex_dot_metacharacter(self):
        """Testa la ricerca con metacarattere punto."""
        # Trova tutti i simboli che contengono "f" seguito da qualsiasi carattere e poi "r"
        results = CuteSymbols.search("f.r")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], ("Emotion", "FIRE", "🔥"))

    def test_search_regex_quantifiers(self):
        """Testa la ricerca con quantificatori regex."""
        # Trova simboli che contengono una o più "s" (lowercase)
        results = CuteSymbols.search("s+")
        expected_names = ["SUCCESS", "HOURGLASS"]
        found_names = [result[1] for result in results]
        for name in expected_names:
            self.assertIn(name, found_names)

    def test_search_regex_alternation(self):
        """Testa la ricerca con alternanza regex."""
        # Trova simboli che contengono "fire" o "water"
        results = CuteSymbols.search("fire|water")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], ("Emotion", "FIRE", "🔥"))

    def test_search_whitespace_handling(self):
        """Testa la gestione degli spazi nella ricerca."""
        results = CuteSymbols.search("  fire  ")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], ("Emotion", "FIRE", "🔥"))

        results = CuteSymbols.search("\tfire\n")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], ("Emotion", "FIRE", "🔥"))

    def test_search_no_results(self):
        """Testa la ricerca senza risultati."""
        results = CuteSymbols.search("xyz")
        self.assertEqual(len(results), 0)

        results = CuteSymbols.search("🦄")
        self.assertEqual(len(results), 0)

        results = CuteSymbols.search("^z")
        self.assertEqual(len(results), 0)

    def test_search_invalid_regex(self):
        """Testa la gestione di regex non valide."""
        with self.assertRaises(ValueError) as context:
            CuteSymbols.search("[")
        self.assertIn("Pattern regex not valid", str(context.exception))

        with self.assertRaises(ValueError) as context:
            CuteSymbols.search("(")
        self.assertIn("Pattern regex not valid", str(context.exception))

        with self.assertRaises(ValueError) as context:
            CuteSymbols.search("*")
        self.assertIn("Pattern regex not valid", str(context.exception))

    def test_search_with_custom_flags(self):
        """Testa la ricerca con flag personalizzati."""
        # Test con multiline flag - ora dovrebbe trovare "FIRE" perché IGNORECASE viene aggiunto automaticamente
        results = CuteSymbols.search("^fire", flags=re.MULTILINE)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], ("Emotion", "FIRE", "🔥"))

        # Test con dotall flag - cerca pattern più complesso
        results = CuteSymbols.search("f.*e", flags=re.DOTALL)
        self.assertEqual(len(results), 3)
        expected_results = [
            ("Emotion", "FIRE", "🔥"),
            ("State", "FAILURE", "✖️"),
            ("Objects", "FOLDER", "📁")
        ]
        for expected in expected_results:
            self.assertIn(expected, results)

    def test_search_partial_matches(self):
        """Testa la ricerca con corrispondenze parziali."""
        # Test ricerca parziale
        results = CuteSymbols.search("fir")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], ("Emotion", "FIRE", "🔥"))

        # Test ricerca con pattern nel mezzo
        results = CuteSymbols.search("ur")
        expected_names = ["HOURGLASS"]
        found_names = [result[1] for result in results]
        for name in expected_names:
            self.assertIn(name, found_names)

    def test_search_special_characters(self):
        """Testa la ricerca con caratteri speciali."""
        # Test ricerca dell'emoji checkmark
        results = CuteSymbols.search("✅")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], ("State", "CHECK", "✅"))

        # Test ricerca con escape di caratteri speciali
        # Il punto interrogativo non esiste nei nostri simboli come carattere regex
        # ma esiste come emoji, quindi non troverà nulla con \\?
        results = CuteSymbols.search("\\?")
        self.assertEqual(len(results), 0)  # Non trova nulla perché cerca letteralmente "?"

    def test_search_multiple_results(self):
        """Testa la ricerca con risultati multipli."""
        # Ricerca che dovrebbe restituire più risultati
        results = CuteSymbols.search("e")
        self.assertGreater(len(results), 1)

        # Verifica che tutti i risultati contengano 'e' (case-insensitive)
        for group, name, value in results:
            self.assertTrue("e" in name.lower() or "e" in value.lower())

    def test_search_word_boundaries(self):
        """Testa la ricerca con confini di parola."""
        # Test ricerca di parole complete (lowercase perché convertito)
        results = CuteSymbols.search("\\bfire\\b")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], ("Emotion", "FIRE", "🔥"))

        # Test che non dovrebbe trovare nulla
        results = CuteSymbols.search("\\bfir\\b")
        self.assertEqual(len(results), 0)

    def test_search_numeric_patterns(self):
        """Testa la ricerca con pattern numerici."""
        # Test con pattern che cerca cifre
        results = CuteSymbols.search("\\d+")
        self.assertEqual(len(results), 0)

        # Test con pattern che cerca caratteri NON numerici
        # Nota: questo pattern matcha qualsiasi stringa che contiene almeno un carattere non numerico
        # Dato che tutti i nostri simboli contengono solo lettere, dovrebbe matchare tutti
        # MA il pattern viene applicato sia al nome che all'emoji, quindi potrebbe non matchare tutti
        results = CuteSymbols.search(".")  # Qualsiasi carattere
        self.assertEqual(len(results), 23)  # Dovrebbe trovare tutti i simboli

    def test_search_integration_with_other_methods(self):
        """Testa l'integrazione della ricerca con altri metodi."""
        # 1. Cerca simboli con regex
        results = CuteSymbols.search("^f")
        self.assertGreater(len(results), 0)

        # 2. Per ogni risultato, verifica che info_from_emoji funzioni
        for group, name, value in results:
            info = CuteSymbols.info_from_emoji(value)
            self.assertIsNotNone(info)
            self.assertEqual(info, (name, group))

    def test_print_table_no_exception(self):
        """Testa che print_table non sollevi eccezioni."""
        try:
            CuteSymbols.print_table()
        except Exception as e:
            self.fail(f"print_table ha sollevato un'eccezione: {e}")

    def test_static_method_access(self):
        """Testa l'accesso ai metodi statici."""
        # Verifica che i metodi statici siano accessibili sia dalla classe che dall'istanza
        self.assertEqual(CuteSymbols.list_all(), self.cute_symbols.list_all())
        self.assertEqual(CuteSymbols.search("fire"), self.cute_symbols.search("fire"))
        self.assertEqual(CuteSymbols.info_from_emoji("🔥"), self.cute_symbols.info_from_emoji("🔥"))
        self.assertEqual(CuteSymbols.name_from_emoji("🔥"), self.cute_symbols.name_from_emoji("🔥"))

    def test_integration_workflow(self):
        """Testa un workflow completo di utilizzo."""
        # 1. Ottieni tutti i simboli
        all_symbols = CuteSymbols.list_all()
        self.assertGreater(len(all_symbols), 0)

        # 2. Cerca un simbolo con regex (pattern lowercase)
        fire_results = CuteSymbols.search("^fire$")
        self.assertEqual(len(fire_results), 1)

        # 3. Ottieni informazioni dall'emoji
        info = CuteSymbols.info_from_emoji("🔥")
        self.assertEqual(info, ("FIRE", "Emotion"))

        # 4. Ottieni il nome dall'emoji
        name = CuteSymbols.name_from_emoji("🔥")
        self.assertEqual(name, "FIRE")

        # 5. Accedi tramite proxy
        self.assertEqual(self.cute_symbols.FIRE, "🔥")

    def test_emoji_uniqueness(self):
        """Testa che ogni emoji sia unico."""
        all_symbols = CuteSymbols.list_all()
        emojis = [symbol[2] for symbol in all_symbols]

        # Verifica che non ci siano emoji duplicate
        self.assertEqual(len(emojis), len(set(emojis)))

    def test_name_uniqueness(self):
        """Testa che ogni nome sia unico."""
        all_symbols = CuteSymbols.list_all()
        names = [symbol[1] for symbol in all_symbols]

        # Verifica che non ci siano nomi duplicati
        self.assertEqual(len(names), len(set(names)))

    def test_search_performance_edge_cases(self):
        """Testa casi limite per le performance del metodo search."""
        # Test con pattern molto generico
        results = CuteSymbols.search(".*")
        self.assertEqual(len(results), 23)  # Dovrebbe trovare tutti i simboli

        # Test con pattern specifico (lowercase)
        results = CuteSymbols.search("^fire$")
        self.assertEqual(len(results), 1)

        # Test con pattern che non matcha nulla
        results = CuteSymbols.search("^nonexistent$")
        self.assertEqual(len(results), 0)

    def test_case_insensitive_namespace(self):
        """Test che l'accesso ai simboli sia case insensitive."""

        # Test con simboli di ogni categoria
        test_cases = [
            # (nome_originale, varianti_case, emoji_atteso)
            ("FIRE", ["fire", "Fire", "FIRE", "fIrE", "FiRe"], "🔥"),
            ("CHECK", ["check", "Check", "CHECK", "cHeCk", "ChEcK"], "✅"),
            ("ROCKET", ["rocket", "Rocket", "ROCKET", "rOcKeT", "RoCkEt"], "🚀"),
            ("FOLDER", ["folder", "Folder", "FOLDER", "fOlDeR", "FoLdEr"], "📁"),
            ("WARNING", ["warning", "Warning", "WARNING", "wArNiNg"], "⚠️"),
            ("HOURGLASS", ["hourglass", "Hourglass", "HOURGLASS", "hOuRgLaSs"], "⏳"),
            ("BRAIN", ["brain", "Brain", "BRAIN", "bRaIn", "BrAiN"], "🧠"),
            ("TOOL", ["tool", "Tool", "TOOL", "tOoL", "ToOl"], "🛠️"),
        ]

        for simbolo_originale, varianti, emoji_atteso in test_cases:
            with self.subTest(simbolo=simbolo_originale):
                # Verifica che l'accesso normale funzioni
                self.assertEqual(getattr(self.cute_symbols, simbolo_originale), emoji_atteso)

                # Verifica che tutte le varianti case insensitive funzionino
                for variante in varianti:
                    with self.subTest(variante=variante):
                        risultato = getattr(self.cute_symbols, variante)
                        self.assertEqual(risultato, emoji_atteso,
                                         f"Accesso case insensitive fallito per '{variante}'. "
                                         f"Atteso: {emoji_atteso}, Ottenuto: {risultato}")

        # Test con simboli che non esistono (case insensitive)
        simboli_inesistenti = ["invalid", "INVALID", "Invalid", "iNvAlId", "notexist", "NOTEXIST"]

        for simbolo_inesistente in simboli_inesistenti:
            with self.subTest(simbolo_inesistente=simbolo_inesistente):
                with self.assertRaises(AttributeError) as context:
                    getattr(self.cute_symbols, simbolo_inesistente)
                self.assertIn(f"Name not found: '{simbolo_inesistente}'", str(context.exception))

        # Test edge cases
        edge_cases = [
            ("cross", "❌"),  # tutto minuscolo
            ("SUCCESS", "✔️"),  # tutto maiuscolo
            ("mAgIc", "✨"),  # case misto casuale
            ("eYeS", "👀"),  # case misto casuale
        ]

        for caso, emoji_atteso in edge_cases:
            with self.subTest(edge_case=caso):
                risultato = getattr(self.cute_symbols, caso)
                self.assertEqual(risultato, emoji_atteso,
                                 f"Edge case fallito per '{caso}'. "
                                 f"Atteso: {emoji_atteso}, Ottenuto: {risultato}")

        # Test che verifica che tutti i simboli siano accessibili in modo case insensitive
        tutti_i_simboli = self.cute_symbols.list_all()

        for gruppo, nome, emoji in tutti_i_simboli:
            with self.subTest(simbolo_completo=f"{gruppo}.{nome}"):
                # Test lowercase
                risultato_lower = getattr(self.cute_symbols, nome.lower())
                self.assertEqual(risultato_lower, emoji,
                                 f"Accesso lowercase fallito per {nome}")

                # Test uppercase (dovrebbe funzionare anche se è già uppercase)
                risultato_upper = getattr(self.cute_symbols, nome.upper())
                self.assertEqual(risultato_upper, emoji,
                                 f"Accesso uppercase fallito per {nome}")


if __name__ == '__main__':
    unittest.main()
