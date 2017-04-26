from mpi4py import MPI
from random import randint

def main():
	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()
	size = comm.Get_size()

	if rank == 0:

		r,c = 102, 102;
		master = [[0 for x in range(r)] for y in range(c)]

		for x in range(r):
			for y in range(c):
				master[x][y] = randint(0,1)

		for x in range(c):
			master[0][x] = 2
			master[101][x] = 2
			master[x][0] = 2
			master[x][101] = 2

		proc = size - 1
		quad_width = 100//(proc)
		quad_width_plus = 100 - (c * (proc - 1))
		
		quad_start = 1
		quads = []
		a_quad = []
		for i in range(proc - 1):
			for j in range(quad_start - 1, quad_start + quad_width + 1):
				for k in range(102):
					a_quad[k][j] = master[k][j]
			quads.append[a_quad]
			quad_start += quad_width
		for j in range(quad_start - 1, quad_start + quad_width_plus + 1):
			for k in range(102):
				a_quad[k][j] = master[k][j]
		quads.append[a_quad]
		
		for i in range(proc):
			print(quads[i], "\n___________________________________")
	


if __name__ == '__main__':
	main()


