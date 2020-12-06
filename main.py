from commenUtils import get_input_data
import logging
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--log", default="info")

options = parser.parse_args()
levels = {'info': logging.INFO, 'debug': logging.DEBUG}

level = levels.get(options.log.lower())

logging.basicConfig(format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
                    level=level)

logger = logging.getLogger(__name__)


def solution_part_1(file_name: str) -> int:
    answers_per_group_per_person: list[list[str]] = get_input_data(file_name)
    sum_yes_answers: int = 0
    current_group_anwers: set[str]
    for answers_per_group in answers_per_group_per_person:
        current_group_anwers = set()
        for answers_per_person in answers_per_group:
            for answer in answers_per_person:
                current_group_anwers.add(answer)
        logger.debug(current_group_anwers)
        sum_yes_answers += len(current_group_anwers)
    return sum_yes_answers


def all_persons_contain_answer(answer: str, answers_per_person: list[str]) -> bool:
    for answers in answers_per_person:
        if not (answer in answers):
            return False
    return True


def solution_part_2(file_name: str) -> int:
    answers_per_group_per_person: list[list[str]] = get_input_data(file_name)
    sum_all_yes: int = 0
    for answers_per_group in answers_per_group_per_person:
        for answer in answers_per_group[0]:
            sum_all_yes += int(all_persons_contain_answer(answer, answers_per_group[1:]))
    return sum_all_yes


if __name__ == '__main__':
    logger.info(solution_part_1("inputData.txt"))
    logger.info(solution_part_2("inputData.txt"))
