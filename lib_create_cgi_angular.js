angular.module('libApp', []).controller('LibController', ['$scope', function ($scope) {

    $scope.phrases = [];

    $scope.addPhrase = function() {
        $scope.phrases.push({
            text: '',
            speechPart: '',
            tail: '',
            paragraph: ''
        });
    }

}]);