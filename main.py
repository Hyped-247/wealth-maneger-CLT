from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError


style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})


class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a valid number',
                cursor_position=len(document.text))  # Move cursor to end


print('Hi, welcome to best investment calculator')

questions = [
    {
        'type': 'input',
        'name': 'passive_income_desired_yearly',
        'message': 'How much passive income do you desire yearly?',
        'validate': NumberValidator
    },
    {
        'type': 'input',
        'name': 'yearly_savings',
        'message': 'How much money are you willing to invest every year?',
        'validate': NumberValidator
    },
    {
        'type': 'input',
        'name': 'starting_year',
        'message': 'What year are you going to start investing? ex. 2030',
        'validate': NumberValidator
    },
    {
        'type': 'input',
        'name': 'price_of_one_apt',
        'message': 'How much does it cost to buy an apartment?',
        'validate': NumberValidator
    },
    {
        'type': 'input',
        'name': 'price_of_renting_one_apt',
        'message': 'How much does renting an apartment yearly cost?',
        'validate': NumberValidator
    },
]


if __name__ == "__main__":
    from pyfiglet import Figlet
    from wealth_manger import Calculator
    f = Figlet(font='slant')
    print(f.renderText('Real estate investment calculator'))
    answers = prompt(questions, style=style)
    passive_income_desired_yearly = int(answers.get('passive_income_desired_yearly'))
    yearly_savings = int(answers.get('yearly_savings'))
    starting_year = int(answers.get('starting_year'))
    price_of_one_apt = int(answers.get('price_of_one_apt'))
    price_of_renting_one_apt = int(answers.get('price_of_renting_one_apt'))
    object_calculator = Calculator(passive_income_desired_yearly,
                                   yearly_savings,
                                   starting_year,
                                   price_of_one_apt,
                                   price_of_renting_one_apt)
    object_calculator.print_results()
