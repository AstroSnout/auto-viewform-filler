import splinter
import random
import threading
from time import sleep


def do_the_thing():
    with splinter.Browser() as browser:
        # Form in question
        url = 'https://docs.google.com/forms/d/e/1FAIpQLSdA9tOw_jaq0vKFQ8BccjGVy1u733LuZyhHvYsE3Mgc4DgB1w/viewform'
        browser.visit(url)
        # Class name of a div containing a question
        question_div_class = '.freebirdFormviewerViewItemsItemItem'
        # Class name of a div containing the option button
        button_div_class = '.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl'
        # Class name of a span containing the submit button
        submit_span_class = '.quantumWizButtonPaperbuttonLabel.exportLabel'
        # Class name of a div containing grid table thing
        grid_div_class = '.freebirdFormviewerViewItemsGridPinnedHeader'
        # Class name of a div containing grid table row
        row_div_class = '.freebirdFormviewerViewItemsGridRow'
        # Class name of a div containing grid table row cell
        cell_div_class = '.quantumWizTogglePaperradioEl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.isDisabled'

        # Gets all the question divs
        all_questions = browser.find_by_css(question_div_class)

        # Choose a random response for every question
        for i in range( len(all_questions) ):
            question = all_questions[i]
            try:
                grid_table = question.find_by_css(grid_div_class)
                grid_rows = grid_table[0].find_by_css(row_div_class)
                # Remove first element cause it's not an actual thing you need to fill up
                grid_rows.pop(0)
                for row in grid_rows:
                    options = row.find_by_css(cell_div_class)
                    print(options)
                    choice = random.randrange(len(options)-1)
                    options[choice+1].click()
            except splinter.exceptions.ElementDoesNotExist:
                print('Element was not found :(')
                pass

            try:
                options = question.find_by_css( button_div_class )
                choice = random.randrange( len(options) )
                options[choice].click()
            except:
                pass

        # Find and press the submit button
        #submit_button = browser.find_by_css( submit_span_class )
        #submit_button.first.click()
        sleep(5)

    return


threads = []
i = 0
while True:
    if len(threads) < 1:
        t = threading.Thread(target=do_the_thing, args=())
        t.start()
        print('Opened thread', i)
        i += 1
        threads.append(t)
    if not threads[0].is_alive():
        threads.pop(0)
        print('Thread removed')


