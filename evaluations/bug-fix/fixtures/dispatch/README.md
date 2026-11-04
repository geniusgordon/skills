# Order dispatch

Submit an order with:

```sh
python3 orders.py --store orders.json --request-id request-1 --item book
```

`--lose-response` simulates a lost reply after storage commits. The caller retries the same request ID and item. A successful retry must return the original order without another stored order.

Different request IDs represent separate orders, even when the items match. Reusing a request ID with a different item must fail without changing storage.

This CLI processes requests sequentially. Concurrent processes and crash-safe file replacement are outside its current contract.
