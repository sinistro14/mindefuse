#! usr/bin/env python3.7

from mindefuse.strategy import StrategyTypes


class EvaluationSuite:
    """
    Parameters to use during the evaluation tests
    """

    suite = [
        # rounds, secret, algorithm
        (12, ["12", "80", "05", "25", "52", "40", "10", "35", "88", "25"], [StrategyTypes.KNUTH, StrategyTypes.GENETIC, StrategyTypes.SWASZEK],),
        #(12, ["880", "030", "307", "036", "564", "855", "719", "512", "856", "085"], [StrategyTypes.KNUTH, StrategyTypes.GENETIC, StrategyTypes.SWASZEK],),
        #(12, ["1056", "9702", "2633", "9426", "9486", "5012", "0508", "0676", "0148", "0935"], [StrategyTypes.KNUTH, StrategyTypes.GENETIC, StrategyTypes.SWASZEK],),

        #(20, ["jv", "nx", "us", "ad", "yy", "qa", "vy", "yl", "ds", "ui"], [StrategyTypes.KNUTH, StrategyTypes.GENETIC, StrategyTypes.SWASZEK],),
        #(20, ["yqq", "slp", "duo", "cuk", "eos", "uuz", "vbr", "uqp", "dgo", "ptj"], [StrategyTypes.GENETIC, StrategyTypes.SWASZEK],),  # Knuth takes too long to be viable, 1 hour in a good case
        #(20, ["jgsf", "moho", "ubbx", "qrlp", "vkcs", "yxgk", "peys", "kxiw", "didc", "kvqk"], [StrategyTypes.GENETIC, StrategyTypes.SWASZEK],),

        #(30, ["vB", "Ic", "lB", "Fm", "ZR", "Gu", "Eq", "fB", "UN", "Wy"], [StrategyTypes.GENETIC, StrategyTypes.SWASZEK],),  # Knuth takes too long to be viable, 12 mins in a good case, and 21 rounds
        #(30, ["hXH", "ojF", "TbG", "PJP", "Hwl", "DMX", "zEc", "IRA", "xzS", "dnM"], [StrategyTypes.GENETIC, StrategyTypes.SWASZEK],),
        #(30, ["SNie", "raNz", "fMjM", "DPIe", "mOiz", "KcFf", "czHG", "QIfl", "yWdV", "GCOL"], [StrategyTypes.GENETIC, StrategyTypes.SWASZEK],),
    ]
