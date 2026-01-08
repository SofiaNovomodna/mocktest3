def f(cars, order):
    if order == 1:
        # sort alphabetically by registration number
        return sorted(cars, key=lambda d: list(d.keys())[0])
    
    elif order == 2:
        # sort by kilometers traveled (descending)
        return sorted(cars, key=lambda d: list(d.values())[0], reverse=True)
    
cars = [{"KR333":138},{"WL555":497},{"DB444":341},{"MC222":412}]
print(f(cars,1))# returns [{"DB444":341},{"KR333":138},{"MC222":412},{"WL555":497}]
print(f(cars,2))# returns [{"WL555":497},{"MC222":412},{"DB444":341},{"KR333":138}]