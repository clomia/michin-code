# https://programmers.co.kr/learn/courses/30/lessons/42840

from functools import reduce


def solution(answer):
    return (
        [
            sorted(
                [
                    (
                        1,
                        reduce(
                            lambda T, S: T + [(S[0] + 1) % 5 == S[1]]
                            if (S[0] + 1) % 5 != 0
                            else T + [5 == S[1]],
                            enumerate(answer),
                            [],
                        ).count(True),
                    ),
                    (
                        2,
                        reduce(
                            lambda T, S: T + [S[1] == 2]
                            if S[0] % 2 == 0
                            else (
                                (T + [S[1] == 4 if S[0] % 8 == 5 else S[1] == 5])
                                if S[0] % 8 >= 5
                                else T + [S[1] == S[0] % 8]
                            ),
                            enumerate(answer),
                            [],
                        ).count(True),
                    ),
                    (
                        3,
                        reduce(
                            lambda T, S: T
                            + [
                                {0: 3, 1: 3, 2: 1, 3: 1, 4: 2, 5: 2, 6: 4, 7: 4, 8: 5, 9: 5}.get(
                                    S[0] % 10
                                )
                                == S[1]
                            ],
                            enumerate(answer),
                            [],
                        ).count(True),
                    ),
                ],
                key=lambda a: a[1],
                reverse=True,
            )[0][0]
        ]
        if sorted(
            [
                (
                    1,
                    reduce(
                        lambda T, S: T + [(S[0] + 1) % 5 == S[1]]
                        if (S[0] + 1) % 5 != 0
                        else T + [5 == S[1]],
                        enumerate(answer),
                        [],
                    ).count(True),
                ),
                (
                    2,
                    reduce(
                        lambda T, S: T + [S[1] == 2]
                        if S[0] % 2 == 0
                        else (
                            (T + [S[1] == 4 if S[0] % 8 == 5 else S[1] == 5])
                            if S[0] % 8 >= 5
                            else T + [S[1] == S[0] % 8]
                        ),
                        enumerate(answer),
                        [],
                    ).count(True),
                ),
                (
                    3,
                    reduce(
                        lambda T, S: T
                        + [
                            {0: 3, 1: 3, 2: 1, 3: 1, 4: 2, 5: 2, 6: 4, 7: 4, 8: 5, 9: 5}.get(
                                S[0] % 10
                            )
                            == S[1]
                        ],
                        enumerate(answer),
                        [],
                    ).count(True),
                ),
            ],
            key=lambda a: a[1],
            reverse=True,
        )[0][1]
        not in [
            sorted(
                [
                    (
                        1,
                        reduce(
                            lambda T, S: T + [(S[0] + 1) % 5 == S[1]]
                            if (S[0] + 1) % 5 != 0
                            else T + [5 == S[1]],
                            enumerate(answer),
                            [],
                        ).count(True),
                    ),
                    (
                        2,
                        reduce(
                            lambda T, S: T + [S[1] == 2]
                            if S[0] % 2 == 0
                            else (
                                (T + [S[1] == 4 if S[0] % 8 == 5 else S[1] == 5])
                                if S[0] % 8 >= 5
                                else T + [S[1] == S[0] % 8]
                            ),
                            enumerate(answer),
                            [],
                        ).count(True),
                    ),
                    (
                        3,
                        reduce(
                            lambda T, S: T
                            + [
                                {0: 3, 1: 3, 2: 1, 3: 1, 4: 2, 5: 2, 6: 4, 7: 4, 8: 5, 9: 5}.get(
                                    S[0] % 10
                                )
                                == S[1]
                            ],
                            enumerate(answer),
                            [],
                        ).count(True),
                    ),
                ],
                key=lambda a: a[1],
                reverse=True,
            )[1][1],
            sorted(
                [
                    (
                        1,
                        reduce(
                            lambda T, S: T + [(S[0] + 1) % 5 == S[1]]
                            if (S[0] + 1) % 5 != 0
                            else T + [5 == S[1]],
                            enumerate(answer),
                            [],
                        ).count(True),
                    ),
                    (
                        2,
                        reduce(
                            lambda T, S: T + [S[1] == 2]
                            if S[0] % 2 == 0
                            else (
                                (T + [S[1] == 4 if S[0] % 8 == 5 else S[1] == 5])
                                if S[0] % 8 >= 5
                                else T + [S[1] == S[0] % 8]
                            ),
                            enumerate(answer),
                            [],
                        ).count(True),
                    ),
                    (
                        3,
                        reduce(
                            lambda T, S: T
                            + [
                                {0: 3, 1: 3, 2: 1, 3: 1, 4: 2, 5: 2, 6: 4, 7: 4, 8: 5, 9: 5}.get(
                                    S[0] % 10
                                )
                                == S[1]
                            ],
                            enumerate(answer),
                            [],
                        ).count(True),
                    ),
                ],
                key=lambda a: a[1],
                reverse=True,
            )[2][1],
        ]
        else list(
            map(
                lambda x: x[0],
                filter(
                    lambda x: x[1]
                    == sorted(
                        [
                            (
                                1,
                                reduce(
                                    lambda T, S: T + [(S[0] + 1) % 5 == S[1]]
                                    if (S[0] + 1) % 5 != 0
                                    else T + [5 == S[1]],
                                    enumerate(answer),
                                    [],
                                ).count(True),
                            ),
                            (
                                2,
                                reduce(
                                    lambda T, S: T + [S[1] == 2]
                                    if S[0] % 2 == 0
                                    else (
                                        (T + [S[1] == 4 if S[0] % 8 == 5 else S[1] == 5])
                                        if S[0] % 8 >= 5
                                        else T + [S[1] == S[0] % 8]
                                    ),
                                    enumerate(answer),
                                    [],
                                ).count(True),
                            ),
                            (
                                3,
                                reduce(
                                    lambda T, S: T
                                    + [
                                        {
                                            0: 3,
                                            1: 3,
                                            2: 1,
                                            3: 1,
                                            4: 2,
                                            5: 2,
                                            6: 4,
                                            7: 4,
                                            8: 5,
                                            9: 5,
                                        }.get(S[0] % 10)
                                        == S[1]
                                    ],
                                    enumerate(answer),
                                    [],
                                ).count(True),
                            ),
                        ],
                        key=lambda a: a[1],
                        reverse=True,
                    )[0][1],
                    sorted(
                        [
                            (
                                1,
                                reduce(
                                    lambda T, S: T + [(S[0] + 1) % 5 == S[1]]
                                    if (S[0] + 1) % 5 != 0
                                    else T + [5 == S[1]],
                                    enumerate(answer),
                                    [],
                                ).count(True),
                            ),
                            (
                                2,
                                reduce(
                                    lambda T, S: T + [S[1] == 2]
                                    if S[0] % 2 == 0
                                    else (
                                        (T + [S[1] == 4 if S[0] % 8 == 5 else S[1] == 5])
                                        if S[0] % 8 >= 5
                                        else T + [S[1] == S[0] % 8]
                                    ),
                                    enumerate(answer),
                                    [],
                                ).count(True),
                            ),
                            (
                                3,
                                reduce(
                                    lambda T, S: T
                                    + [
                                        {
                                            0: 3,
                                            1: 3,
                                            2: 1,
                                            3: 1,
                                            4: 2,
                                            5: 2,
                                            6: 4,
                                            7: 4,
                                            8: 5,
                                            9: 5,
                                        }.get(S[0] % 10)
                                        == S[1]
                                    ],
                                    enumerate(answer),
                                    [],
                                ).count(True),
                            ),
                        ],
                        key=lambda a: a[1],
                        reverse=True,
                    ),
                ),
            )
        )
    )
