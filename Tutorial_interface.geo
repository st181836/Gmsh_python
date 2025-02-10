// Gmsh project created on Sun Feb 02 20:08:57 2025
//+
Point(1) = {1.4, 1.2, 0, 1.0};
//+
Recursive Delete {
  Point{1}; 
}
//+
Point(1) = {0, 0, 0, 1.0};
//+
Point(2) = {5, 0, 0, 1.0};
//+
Point(3) = {5, 5, 0, 1.0};
//+
Point(4) = {5, 4, 0, 1.0};
//+
Point(5) = {4, 5, 0, 1.0};
//+
Recursive Delete {
  Point{4}; 
}
//+
Line(1) = {1, 2};
//+
Line(2) = {2, 3};
//+
Line(3) = {3, 5};
//+
Line(4) = {5, 1};
//+
Curve Loop(1) = {4, 1, 2, 3};
//+
Plane Surface(1) = {1};
//+
Physical Curve("inlet", 5) = {3};
//+
Show "*";
//+
Show "*";
//+
Physical Curve("right edge", 100002) = {4, 2};
