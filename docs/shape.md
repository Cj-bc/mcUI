 This is document for shape

* contents
  |how-to-shape| --- literally
    -- |how-they-get-shaped| --- how they get shaped
    -- |basic-idea-of-shaping| --- basement idea.
    -- |parameters| --- all parameters to shape
  |shape|  --- all shapes already avilable





                      *how to shape*
   Instead of using default shapes, you can use your own shapes
  for directory and files.
   Here're simple reference for it.

    *how they get shaped*
        shapes are defined in *shape* class
        each methods in it is the blueprint for each shape
        in *builder* class, at *builddir* and *buildfile* method,
        they get shaped
        
    *Basic Idea of shaping*
       As avilable API to put block is only setBlock() and setBlocks(),
      What we can shape is based rectangular and dots.
      Basically, all things are devided into some rectangulars. 
      By combine rectanglars, we shape them

    *parameters*
        blocks --- devided rectangular shapes
                   if there some rec.s, you can use this as List of List
                   usage:
                     blocks = [[x1,y1,z1],[x2,y2,z2]..]



                        *shape*
  here is all sort of shapes included by default
  * Lists
    |default_Rectanglar|



  # default_Rectangular

      this is the simplest shape.

           _________.                 | looks like: rectangular
          /        /|                 | scale:      10x5x10 blocks
         /        / |                 | color:      default_color
        /        /  |
       /--------/   |
       |        |   /
       |        |  /
       |        | /
       ----------/
