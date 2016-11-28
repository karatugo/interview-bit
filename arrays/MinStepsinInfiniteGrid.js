module.exports = {
    //param A : array of integers
    //param B : array of integers
    //return an integer
    coverPoints: function(A, B) {
        var numberOfSteps = 0;

        if (A.length < 2) {
            return 0;
        }

        for (i = 0; i < A.length - 1; i++) {
            var firstPoint = [A[i], B[i]];
            var secondPoint = [A[i + 1], B[i + 1]];
            var shiftedSecondPoint = shiftSecondPoint(firstPoint, secondPoint);
            var reflectedAndShifted = reflectShiftedSecondPoint(shiftedSecondPoint);
            numberOfSteps += reflectedAndShifted[1];
        }

        return numberOfSteps;

        function shiftSecondPoint(firstPoint, secondPoint) {
            var x = Math.abs(secondPoint[0] - firstPoint[0]);
            var y = Math.abs(secondPoint[1] - firstPoint[1]);
            return [x, y];
        }

        function reflectShiftedSecondPoint(shiftedSecondPoint) {
            if (shiftedSecondPoint[0] > shiftedSecondPoint[1]) {
                return [shiftedSecondPoint[1], shiftedSecondPoint[0]];
            }

            return [shiftedSecondPoint[0], shiftedSecondPoint[1]];
        }

    }
};