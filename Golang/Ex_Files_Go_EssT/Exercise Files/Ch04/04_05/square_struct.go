package main

import (
		"fmt"
)

// Point is a 2d point
type Point struct {
		X int
		Y int
}

// Move moves the point
func (p *Point) Move(dx int, dy int) {
		p.X += dx
		p.Y += dy
}

type Square struct{
		Center Point
		Length int
}

func NewSquare(x int, y int, length int) (*Square, error) {
		if length <= 0 {
				return nil, fmt.Errorf("Length must bed greater than 0"
		}

		square := &Square{
				Center: Point{x, y},
				Length: length,
		}
		return square, nil

}
func (s *Square) Move(dx int, dy int) {
		s.Center.Move(dx,dy)
}

func (s *Square) Area() int {
		return s.Length * 2
}

func main() {
		sq, _ := NewSquare(1,2,3)
		fmt.Println(sq)
		sq.Move(1,1)
		fmt.Println(sq)

}
