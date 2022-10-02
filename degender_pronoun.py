from string import punctuation

class degenderizer():
    def __init__(self):
        # Lists with words that frequently follow possesive pronouns. 
        # punctuations
        self._punc = list(punctuation)
        
        # mapping gender pronouns and neutral pronouns
        
        #Default list of dictionary values.
        #Must be [he/she, him/her, his/her, his/hers, himself/herself]
        self.default_set = ["they", "them", "their", "theirs", "themselves"]
        
        self._dictionary1, self._dictionary2 = self._initDict(pron_set=self.default_set)
        self._mapping = self._updateMapping()
        
    def _initDict(self, pron_set):
        dict1 ={"s/he":pron_set[0],
                "{s}he":pron_set[0],
                "he or she":pron_set[0],
                "she or he":pron_set[0],
                "he/she": pron_set[0],
                "she/he": pron_set[0],
                "he / she": pron_set[0],
                "she / he": pron_set[0],
                "he/ she": pron_set[0],
                "she/ he": pron_set[0],
                "herself":pron_set[4],
                "himself":pron_set[4],
                "him":pron_set[1],
                "hers":pron_set[3],
                "she":pron_set[0],
                "he":pron_set[0],
                }
        
        dict2 = {"her (obj)":pron_set[1],
                        "her (adj)": pron_set[2],
                        "his (adj)": pron_set[2],
                        "his (possess)": pron_set[3]
                        }
        return dict1, dict2
        
        
    def _updateMapping(self):
        mapping = []
        for pron_a, pron_b in self._dictionary1.items():
            cases = [(pron_a.lower(), pron_b.lower()), (pron_a.upper(), pron_b.upper()), (pron_a.title(), pron_b.title())]
            for case in cases:
                a, b = case[0], case[1]
                mapping.append((" {} ".format(a), " {} ".format(b)))
                for p in self._punc:
                    mapping.append(("{0}{1} ".format(p,a), "{0}{1} ".format(p,b)))
                    mapping.append((" {0}{1}".format(a,p), " {0}{1}".format(b,p)))
                    for pp in self._punc:
                        mapping.append(("{0}{1}{2}".format(p,a,pp), "{0}{1}{2}".format(p,b,pp)))
        return mapping
        
    def _replaceHisHer(self, text):
        '''
        This function replaces his/her in dictionary2.

        Parameters
        ----------
        text : String.
            An English sentence to be processed.

        Returns
        -------
        String.
            Replaced sentence.

        '''
        if not isinstance(text, str):
            text = str(text)
            
        _conjs = set(["after", "although", "and", "as", "because", "before", "but", "by", "even", "if", "in",
                             "lest", "once", "only", "or", "provided", "since", "so", "than", "that", "though",
                             "till", "unless", "until", "when", "whenever", "where", "wherever", "whether", "while"])
        _preps = set([ "a", "aboard", "about", "above","across", "after", "against", "along", "amid", "among",
                             "an","anti", "around", "as", "at", "before", "behind", "below", "beneath", "beside", "besides",
                             "between", "beyond", "but", "by", "concerning", "considering", "despite", "down", "during",
                             "except", "excepting", "excluding", "following", "for", "from", "in", "inside", "into", "like",
                             "minus", "near", "of", "off", "on", "onto", "opposite", "outside", "over", "past", "per", "plus",
                             "regarding", "round", "save", "since", "than", "the", "through", "to", "toward", "towards", "under",
                             "underneath", "unlike", "until", "up", "upon", "versus", "via", "with", "within", "without" ])
        
        his_cases = ["his", "His", "HIS"]
        her_cases = ["her", "Her", "HER"]
        
        _hisPunc = [[h + p for p in self._punc] for h in his_cases]
        _herPunc = [[h + p for p in self._punc] for h in her_cases]
        change_case = [lambda x: x.lower(),
                       lambda x:x.title(),
                       lambda x:x.upper()]

        _follows = set([func(conj) for conj in _conjs for func in change_case]
                       + [func(prep) for prep in _preps for func in change_case]
                       + self._punc)
        
        his_a = self._dictionary2["his (adj)"]
        his_n = self._dictionary2["his (possess)"]
        her_n = self._dictionary2["her (obj)"]
        her_a = self._dictionary2["her (adj)"]
        
        # split tokens by space, and remove null string
        tokens = [token for token in text.split(" ") if token not in ["", "\n", "\r"]]
        
        # Iterate over tokens while looking ahead one token.
        for i in range(len(tokens)-1):
            for j in range(len(change_case)):
                if tokens[i] in _hisPunc[j]:
                    tokens[i] = change_case[j](his_n)+ tokens[i][-1]
                elif tokens[i] == his_cases[j] and tokens[i+1] in _follows:
                    tokens[i] = change_case[j](his_n)
                elif tokens[i] == his_cases[j]:
                    tokens[i] = change_case[j](his_a)
                    
                if tokens[i] in _herPunc[j]:
                    tokens[i] = change_case[j](her_n) + tokens[i][-1]
                elif tokens[i] == her_cases[j] and tokens[i+1] in _follows:
                    tokens[i] = change_case[j](her_n)
                elif tokens[i] == her_cases[j]:
                    tokens[i] = change_case[j](her_a)
                
        # Check last token.
        last = -1
        for j in range(len(change_case)):
            if tokens[last] in _hisPunc[j]:
                tokens[last] = change_case[j](his_n)+ tokens[last][-1]
            if tokens[last] in his_cases:
                tokens[last] = change_case[j](his_n)
                
            if tokens[last] in _herPunc[j]:
                tokens[last] = change_case[j](her_n) + tokens[last][-1]
            if tokens[last] in her_cases:
                tokens[last] = change_case[j](her_n)
            
        return " ".join(tokens)
    
    def _replaceOther(self, text):
        '''
        Replace pronouns other than his and her.

        Parameters
        ----------
        text : String.
            An English sentence to be processed.

        Returns
        -------
        text : String.
            Replaced sentence.

        '''
        if isinstance(text, str):
            text = str(text)
        text = " " + text + " "
        for k, v in self._mapping:
            text = text.replace(k,v)
        return text
    
        
    def getDictionary(self):
        '''
        Get the current dictionary.

        Returns
        -------
        set
            The dictionary.

        '''
        
        return self.default_set
    
    def setDictionary(self, user_set):
        '''
        Replace the default dictionary and mapping with the user set one.

        Parameters
        ----------
        user_set : List.
            A list of dictionary values.
            Must be [he/she, him/her, his/her, his/hers, himself/herself]

        Returns
        -------
        None.

        '''
        self.default_set = user_set
        self._dictionary1, self._dictionary2 =  self._initDict(pron_set=self.default_set)
        self._mapping = self._updateMapping()
        
    def degender(self, text):
        '''
        Takes an english text string and makes all pronouns gender neutral.

        Parameters
        ----------
        text : String.
            An English sentence to be processed.

        Returns
        -------
        text2 : String.
            Replaced sentence.

        '''

        text1 = self._replaceOther(text)
        text2 = self._replaceHisHer(text1)
        return text2