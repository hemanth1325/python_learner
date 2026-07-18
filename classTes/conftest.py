import pytest
# from pathlib import Path
# from tempfile import TemporaryDirectory
import cards
 

def pytest_addoption(parser):
    parser.addoption("--func-db", action="store_true", help="use function scoped db")



def db_scope(fixture_name,config):
    if config.getoption("--func-db",None):
        return "function"
    return "session"


# @pytest.fixture(scope=db_scope)
# def db():
#     with TemporaryDirectory() as db_dir:
#         db_path = Path(db_dir)
#         db = cards.CardsDB(db_path)
#         yield db
#         db.close()



@pytest.fixture(scope=db_scope)
def db(tmp_path_factory):
    db_path = tmp_path_factory.mktemp("cards_db")
    db = cards.CardsDB(db_path)
    yield db
    db.close()

 
@pytest.fixture(scope="function")
def cards_db(db,request,faker):
    db.delete_all()
    

    faker.seed_instance(101)
    m=request.node.get_closest_marker("num_cards")
    if m and len(m.args) > 0:
        num_cards = m.args[0]
        for _ in range(num_cards):
            db.add_card(cards.Card(summary=faker.sentence(), owner=faker.name()))
    
    
    
    return db



@pytest.fixture(scope="session")
def some_cards():
    return [ cards.Card("work", "hemanth"),
                cards.Card("send email", "sachin"),
                cards.Card("call", "hemanth")]



@pytest.fixture(scope="function")
def non_empty_db(cards_db, some_cards):
    for c in some_cards:
        cards_db.add_card(c)
    return cards_db




    