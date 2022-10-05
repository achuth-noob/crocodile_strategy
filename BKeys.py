# API_KEY = 'vd77s0EVm4dQrzQjOHATiiPeVwo7J0ESv1AKeFZzBuA2UmLy54gkoNmgJfXaggm8'
# API_SECRET = '9MKvdAlpcQqg2TQIdCc6zWXjQ36cAcBtpf67H78zyNWcZOEFnb64yxJJINVNypCu'

# Abhishek creds
API_KEY = "NVEBIIaTYTlLBfkRfEsqSQeYecsuAyRaaX3MNkB7gDTXvZ8puUNb3MiyLQ2j0ZzO"
API_SECRET = "awaVSqn2Y61l0zEZzWR4cPDBCi9oUdabtYu4mdxx15FZNVWzA8QdPunsXtAfeQir"

# from binance import ThreadedDepthCacheManager
#
# def main():
#
#     dcm = ThreadedDepthCacheManager()
#     # start is required to initialise its internal loop
#     dcm.start()
#
#     def handle_depth_cache(depth_cache):
#         print(f"symbol {depth_cache.symbol}")
#         print("top 5 bids")
#         print(depth_cache.get_bids()[:5])
#         print("top 5 asks")
#         print(depth_cache.get_asks()[:5])
#         print("last update time {}".format(depth_cache.update_time))
#
#     dcm_name = dcm.start_depth_cache(handle_depth_cache, symbol='BNBBTC')
#
#     # multiple depth caches can be started
#     dcm_name = dcm.start_depth_cache(handle_depth_cache, symbol='ETHBTC')
#
#
# if __name__ == "__main__":
#    main()