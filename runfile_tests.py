from runfile import *
import unittest
import os


class Classes(unittest.TestCase):
    def test_inheritance(self):
        albumimage_example = AlbumImage("Unknown Pleasures", "Joy Division" , "https://www.billboard.com/files/styles/900_wide/public/media/Joy-Division-Unknown-Pleasures-album-covers-billboard-1000x1000.jpg")
        artist_example = "Joy Division"
        self.assertEqual(artist_example, albumimage_example.getartist())

class Functions(unittest.TestCase):
    def test_scraping(self):
        self.assertTrue(len(albumdata) > 24)
        self.assertTrue(len(albumdata) < 101)
    def test_path_set_correctly(self):
        self.f = open(image_directory + "testfile.txt")
        self.assertTrue(self.f.read())
        self.f.close()
    def test_image_list(self):
        self.assertEqual(type(image_list[0].getartist()), type(""))
        self.assertTrue(len(image_list) > 24)
        self.assertTrue(len(image_list) < 101)
    def test_dream_url(self):
        x = deep_dream("NO")
        self.assertEqual("https://api.deepai.org", x[:22])
    def test_image_directory(self):
        imagecount = len([1 for x in list(os.scandir(image_directory)) if x.is_file()])
        self.assertTrue(imagecount > 2)
        self.assertTrue(imagecount < 101)
    def test_dream_file(self):
        dreamimage = Image.open(dream_directory)
        self.assertEqual(dreamimage.format, "JPEG")
        dreamimage.close()
    def test_collage_file(self):
        collageimage = Image.open(collage_directory)
        self.assertEqual(collageimage.format, "JPEG")
        collageimage.close()
    def test_print_list(self):
        dummylist = list_albums(collage_images, dummy = "yes")
        self.assertTrue(len(dummylist) == 25)
        self.assertEqual(type(dummylist[0]), type(""))

class Caches(unittest.TestCase):
    def setUp(self):
        self.f = open("project_cache.json")
    def test_file_exists(self):
        self.assertTrue(self.f.read())
    def TearDown(self):
        self.f.close()



























if __name__  == "__main__":
    unittest.main(verbosity=2)
