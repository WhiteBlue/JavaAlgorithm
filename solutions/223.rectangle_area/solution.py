def get_overlap(a1, a2, a3, a4):
    return min(a2, a4) - max(a1, a3)


class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        overlap_acreage = 0
        all_acreage = (C - A) * (D - B) + (G - E) * (H - F)
        overlap_x, overlap_y = get_overlap(A, C, E, G), get_overlap(B, D, F, H)
        if overlap_x > 0 and overlap_y > 0:
            overlap_acreage = overlap_x * overlap_y
        return all_acreage - overlap_acreage
