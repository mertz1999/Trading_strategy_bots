from OpenTrade.strategy_list.reverse_grid import ReverseGrid
import pandas as pd

data = pd.read_csv('./data/BTC_2021.csv')
data = pd.DataFrame(data.values[::-1], data.index, data.columns)


# Grid Trading parameters
High_price         = 100000
Low_price          = 10000
num_grids          = 500 
per_order          = 0.1        # each order = per_order * investment
investment         = 600
fee                = 0.1        # In percent
max_open_positions = 8


st = ReverseGrid(High_price , Low_price, num_grids, per_order, max_open_positions,data,investment, fee, name="ReverseGrid", method="ORDER-FUTURE")
# st.run()
