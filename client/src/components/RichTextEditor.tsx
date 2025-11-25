import { useEditor, EditorContent } from '@tiptap/react';
import StarterKit from '@tiptap/starter-kit';
import CodeBlockLowlight from '@tiptap/extension-code-block-lowlight';
import Youtube from '@tiptap/extension-youtube';
import { common, createLowlight } from 'lowlight';
import 'highlight.js/styles/github.css';

const lowlight = createLowlight(common);

interface RichTextEditorProps {
  content: string;
  editable: boolean;
  onChange?: (content: string) => void;
}

const RichTextEditor = ({ content, editable, onChange }: RichTextEditorProps) => {
  const editor = useEditor({
    extensions: [
      StarterKit.configure({
        codeBlock: false,
      }),
      CodeBlockLowlight.configure({
        lowlight,
      }),
      Youtube.configure({
        controls: true,
      }),
    ],
    content: content,
    editable: editable,
    onUpdate: ({ editor }) => {
      if (onChange) {
        onChange(editor.getHTML());
      }
    },
    editorProps: {
      attributes: {
        class: 'prose prose-sm sm:prose lg:prose-lg xl:prose-2xl mx-auto focus:outline-none min-h-[300px] p-4',
      },
    },
  });

  if (!editor) {
    return null;
  }

  // Update content if it changes externally and editor is not focused (to prevent cursor jumps)
  // This is a simplified approach; ideally we'd use a more robust effect
  if (editor.getHTML() !== content && !editor.isFocused && content) {
      editor.commands.setContent(content);
  }
  
  // Make sure editor editable state matches prop
  if (editor.isEditable !== editable) {
      editor.setEditable(editable);
  }

  return (
    <div className="border rounded-lg bg-white shadow-sm">
      {editable && (
        <div className="border-b p-2 flex flex-wrap gap-2 bg-gray-50 rounded-t-lg">
          <button
            onClick={() => editor.chain().focus().toggleBold().run()}
            className={`p-1 px-2 rounded ${editor.isActive('bold') ? 'bg-gray-200' : 'hover:bg-gray-200'}`}
          >
            Bold
          </button>
          <button
            onClick={() => editor.chain().focus().toggleItalic().run()}
            className={`p-1 px-2 rounded ${editor.isActive('italic') ? 'bg-gray-200' : 'hover:bg-gray-200'}`}
          >
            Italic
          </button>
          <button
            onClick={() => editor.chain().focus().toggleHeading({ level: 2 }).run()}
            className={`p-1 px-2 rounded ${editor.isActive('heading', { level: 2 }) ? 'bg-gray-200' : 'hover:bg-gray-200'}`}
          >
            H2
          </button>
          <button
            onClick={() => editor.chain().focus().toggleBulletList().run()}
            className={`p-1 px-2 rounded ${editor.isActive('bulletList') ? 'bg-gray-200' : 'hover:bg-gray-200'}`}
          >
            Bullet List
          </button>
           <button
            onClick={() => editor.chain().focus().toggleCodeBlock().run()}
            className={`p-1 px-2 rounded ${editor.isActive('codeBlock') ? 'bg-gray-200' : 'hover:bg-gray-200'}`}
          >
            Code Block
          </button>
          <button
            onClick={() => {
              const url = prompt('Enter YouTube URL');
              if (url) {
                editor.commands.setYoutubeVideo({ src: url });
              }
            }}
            className="p-1 px-2 rounded hover:bg-gray-200"
          >
            Add Video
          </button>
        </div>
      )}
      <EditorContent editor={editor} className="p-4" />
    </div>
  );
};

export default RichTextEditor;

