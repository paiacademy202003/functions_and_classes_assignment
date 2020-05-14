class TrendLine:
    def fit(self, X, Y):
        n = len(X)
        q1 = n * sum([X[i] * Y[i] for i in range(n)])
        q2 = sum(X) * sum(Y)
        q3 = n * sum([X[i]**2 for i in range(n)])
        q4 = sum(X)**2
        self.m = (q1 - q2) / (q3 - q4)
        self.b = (sum(Y) - self.m * sum(X)) / n

    def predict(self, X):
        return [self.m * x + self.b for x in X]

    def score(self, X, Y):
        prediction = self.predict(X)
        ybar = sum(Y) / len(Y)
        ss_tot = sum([(Y[i] - ybar) ** 2 for i in range(len(Y))])
        ss_res = sum([(Y[i] - prediction[i]) ** 2 for i in range(len(Y))])
        return 1 - ss_res / ss_tot

if __name__ == '__main__':
    model = TrendLine()
    points = [[1,1],[1,3],[3,4],[3,1],[4,3],[6,4]]
    X = [x[0] for x in points]
    y = [x[1] for x in points]
    model.fit(X,y)
    print(model.m)
    print(model.b)
    score = model.score(X,y)
    print(score)
