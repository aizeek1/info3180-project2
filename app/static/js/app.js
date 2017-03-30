// Your JavaScript Code here
/* global angular */

var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope, $http) {
   $http.get("/api/thumbnails").then(function (response) {
       console.log(response.data.thumbnails);
      $scope.myThumbnails =response.data.thumbnails;
   });
});
