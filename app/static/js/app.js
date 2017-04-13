// Your JavaScript Code here
/* global angular */


var imageapp = angular.module('myApp', []);
imageapp.controller('myImage', function($scope, $http) {
   $http.get("/api/thumbnails").then(function (response) {
       console.log(response.data.thumbnails);
      $scope.myThumbnails =response.data.thumbnails;
   });
});


