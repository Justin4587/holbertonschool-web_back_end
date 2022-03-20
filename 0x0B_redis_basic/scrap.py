    def wrapper(arg):
        _redis.incr(f"count:{arg}")
        cached = _redis.get(f"cached:{arg}")
        if cached:
            return cached.decode('utf-8')
        what = method(arg)
        _redis.setex(f"cached:{arg}", 10, what)
        return what


        print(args[0])
        key = f"count:{args[0]}"
        _redis.incr(key)
        _redis.setex('count', 10, _redis.get(key))
        return method(*args)

        def wrapper(url):
        """something about redis"""
        print(f"this is from args {url}")
        key = f"count:{url}"
        _redis.incr(key)
        _redis.setex('count', 10, _redis.get(key))
        return method(url)