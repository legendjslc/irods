import pydevtest_sessions as s
from nose.tools import with_setup
from nose.plugins.skip import SkipTest
from pydevtest_common import assertiCmd, assertiCmdFail
import commands

@with_setup(s.adminonly_up,s.adminonly_down)
def test_local_imv():
    # local setup
    movedfile = "moved_file.txt"
    # assertions
    assertiCmd(s.adminsession,"imv "+s.testfile+" "+movedfile) # move
    assertiCmd(s.adminsession,"ils -L "+movedfile,"LIST",movedfile) # should be listed
    # local cleanup

@with_setup(s.adminonly_up,s.adminonly_down)
def test_local_imv_to_directory():
    # local setup
    # assertions
    assertiCmd(s.adminsession,"imv "+s.testfile+" "+s.testdir) # move
    assertiCmd(s.adminsession,"ils -L "+s.testdir,"LIST",s.testfile) # should be listed
    # local cleanup

@with_setup(s.adminonly_up,s.adminonly_down)
def test_local_imv_to_existing_filename():
    # local setup
    copyfile = "anotherfile.txt"
    # assertions
    assertiCmd(s.adminsession,"icp "+s.testfile+" "+copyfile) # icp
    assertiCmd(s.adminsession,"imv "+s.testfile+" "+copyfile, "ERROR", "CAT_NAME_EXISTS_AS_DATAOBJ") # cannot overwrite existing file
    # local cleanup
