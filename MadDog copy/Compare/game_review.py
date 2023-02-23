import chess
import chess.pgn
from analize import analize
import io

string_pgn = """[Event "?"]
[Site "?"]
[Date "????.??.??"]
[Round "?"]
[White "?"]
[Black "?"]
[Result "*"]

1. d4 d5 2. c4 e6 3. Nc3 Be7 4. e3 Nf6 5. cxd5 Nbd7 6. Nf3 c6 7. g3 O-O 8. Bd3 Bb4 9. Qc2 Ba5 10. O-O Bb6 11. Re1 cxd5 12. Ne5 Ne4 13. a3 Nef6 14. b3 Bc7 15. h3 Ne4 16. f4 Nef6 17. Ne4 Bd6 18. Bb2 Nxe4 19. Rad1 Nec5 20. e4 Nxd3 21. Rd2 N3xe5 22. dxe5 Be7 23. f5 a6 24. Ree2 Bd6 25. Kg2 Bc7 26. b4 Bb6 27. exd5 Ba5 28. h4 Bb6 29. g4 Ba5 30. Kg3 Bb6 31. Qc3 Rb8 32. h5 f6 33. g5 Nxe5 34. d6 Ng4 35. Kxg4 Bc7 36. Qc4 Bxd6 37. Qc5 Bxc5 38. b5 Bb6 39. a4 Ba5 40. Rd3 Bb6 41. Red2 Qe8 42. Re2 axb5 43. a5 Bc5 44. Red2 Bd6 45. Re2 Be5 46. Red2 Bd6 47. Rd4 Bb4 48. Re2 Bc5 49. Red2 Bd6 50. Rd5 Be5 51. Rd6 Bc3 52. Bxc3 exf5+ 53. Kg3 b6 54. Kf4 Rb7 55. h6 Rb8 56. Re2 Qe7 57. Rf2 Qd7 58. Re2 Qc7 59. Rf2 Qb7 60. Re2 Qf7 61. Red2 Qb7 62. Re2 Qf7 63. Rf2 Re8 64. Rf3 Rb7 65. a6 Rb8 66. Bd4 Re7 67. Re3 Re8 68. Re4 Qf8 69. Re5 Re7 70. Rd7 Re8 71. Kxf5 Rb7 72. g6 Rb8 73. Re6 Re7 74. Rexe7 Qf7 75. Be5 Qf8 76. a7 Qe8 77. Bxf6 Qxe7 78. Kf4 Qe8 79. Kf5 Qe7 80. Kg4 Rb7 81. Kg5 Qe8 82. Kf4 Rb8 83. Kg5 Rb7 84. Kh5 Qe7 85. Rd8+ Qe8 86. hxg7 Rb8 87. Kg5 h6+ 88. Kf4 h5 89. Kf3 Qf8 90. Kf4 Rb7 91. Ke5 Rb8 92. Kd5 Qe8 93. Kd4 Rb7 94. Kd5 Qf8 95. Kc6 Qe8+ 96. Kd6 Rb8 97. Kd5 Qf8 98. Kc6 Rb7 99. Be7 Rb8 100. Kd6 Rb7 101. Ke5 Qe8 102. Kd6 h4 103. Kd5 h3 104. Ke5 h2 105. Kf6 Rc7 106. Rd7 Qxe7+ 107. Kf5 Rc6 108. Kf4 Rc7 109. Kf5 Qe6+ 110. Kg5 Qe7+ *"""

string_pgn = io.StringIO(string_pgn)

game = chess.pgn.read_game(string_pgn)

analizer = analize("Kasparov", game)
analizer.analize()