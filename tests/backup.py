    def test_05_create(self):
        """Test to validate create works."""
        cli = self.create()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("create BaseModel")
        p = r'(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})'
        prog = re.compile(p)
        self.assertNotEqual(None, prog.match(output.getvalue()))
        sys.stdout = sys.__stdout__

    def test_05a_create_bad_value(self):
        """Test to validate create with bad value."""
        cli = self.create()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("create Monster")
        self.assertEqual("** class doesn't exist **\n", output.getvalue())
        sys.stdout = sys.__stdout__

    def test_05b_create_empty_value(self):
        """Test to validate create with empty values."""
        cli = self.create()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("create")
        self.assertEqual("** class name missing **\n", output.getvalue())
        sys.stdout = sys.__stdout__

    def test_05c_create_extra_values(self):
        """Test to validate create with extra empty."""
        cli = self.create()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("create BaseModel hello")
        p = r'(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})'
        prog = re.compile(p)
        self.assertNotEqual(None, prog.match(output.getvalue()))
        sys.stdout = sys.__stdout__

    def test_06a_show(self):
        """Test to validate show works."""
        cli = self.create()
        b = BaseModel()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("show BaseModel " + b.id)
        self.assertTrue(output.getvalue().startswith('[BaseModel]'))
        sys.stdout = sys.__stdout__

    def test_06b_show_missing_class(self):
        """Test for show with missing class."""
        cli = self.create()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("show ")
        self.assertEqual("** class name missing **\n", output.getvalue())
        sys.stdout = sys.__stdout__

    def test_06c_show_missing_id(self):
        """Test for show with missing id."""
        cli = self.create()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("show MyModel")
        self.assertEqual("** class doesn't exist **\n", output.getvalue())
        sys.stdout = sys.__stdout__

    def test_06d_show_missing_class(self):
        """Test for show with missing class."""
        cli = self.create()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("show BaseModel")
        self.assertEqual("** instance id missing **\n", output.getvalue())
        sys.stdout = sys.__stdout__

    def test_06e_show_missing_class(self):
        """Test for show with missing class."""
        cli = self.create()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("show BaseModel 32432423")
        self.assertEqual("** no instance found **\n", output.getvalue())
        sys.stdout = sys.__stdout__

    def test_07_destroy(self):
        """Test to validate destroy works."""
        cli = self.create()
        b = BaseModel()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("destroy BaseModel " + b.id)
        cli.onecmd("show BaseModel " + b.id)
        self.assertEqual("** no instance found **\n", output.getvalue())

    def test_07a_destroy(self):
        """Check destroy with invalid instance."""
        cli = self.create()
        b = BaseModel()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("destroy BaseModel " + b.id)
        cli.onecmd("destroy BaseModel " + b.id)
        self.assertEqual("** no instance found **\n", output.getvalue())

    def test_07b_destroy(self):
        """Check destroy with invalid class."""
        cli = self.create()
        b = BaseModel()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("destroy MyModel " + b.id)
        self.assertEqual("** class doesn't exist **\n", output.getvalue())

    def test_07c_destroy(self):
        """Check destroy without class name."""
        cli = self.create()
        b = BaseModel()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("destroy")
        self.assertEqual("** class name missing **\n", output.getvalue())

    def test_07d_destroy(self):
        """Check destroy without id."""
        cli = self.create()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("destroy BaseModel")
        self.assertEqual("** instance id missing **\n", output.getvalue())

    def test_07e_destroy(self):
        """Test to validate destroy works on different models."""
        cli = self.create()
        b = User()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("destroy User " + b.id)
        cli.onecmd("show User " + b.id)
        self.assertEqual("** no instance found **\n", output.getvalue())

    def test_07f_destroy(self):
        """Test to validate destroy works on different models."""
        cli = self.create()
        b = State()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("destroy State " + b.id)
        cli.onecmd("show State " + b.id)
        self.assertEqual("** no instance found **\n", output.getvalue())

    def test_07g_destroy(self):
        """Test to validate destroy works on different models."""
        cli = self.create()
        b = City()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("destroy City " + b.id)
        cli.onecmd("show City " + b.id)
        self.assertEqual("** no instance found **\n", output.getvalue())

    def test_07h_destroy(self):
        """Test to validate destroy works on different models."""
        cli = self.create()
        b = Amenity()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("destroy Amenity " + b.id)
        cli.onecmd("show Amenity " + b.id)
        self.assertEqual("** no instance found **\n", output.getvalue())

    def test_07i_destroy(self):
        """Test to validate destroy works on different models."""
        cli = self.create()
        b = Place()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("destroy Place " + b.id)
        cli.onecmd("show Place " + b.id)
        self.assertEqual("** no instance found **\n", output.getvalue())

    def test_07j_destroy(self):
        """Test to validate destroy works on different models."""
        cli = self.create()
        b = Review()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("destroy Review " + b.id)
        cli.onecmd("show Review " + b.id)
        self.assertEqual("** no instance found **\n", output.getvalue())

    def test_08_all(self):
        """Test to validate all works."""
        cli = self.create()
        b = BaseModel()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("all")
        # self.assertEqual("** no instance found **\n", output.getvalue())

    def test_09_update(self):
        """Test to validate update works."""
        pass
