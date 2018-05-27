import pytest

class  Test_01:
    @pytest.mark.parametrize("a",[1,2,3,4])
    def test_001(self,a):
        assert  a !=1
if __name__ == '__main__':
    pytest.main("test01.py")